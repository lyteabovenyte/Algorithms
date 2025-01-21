
/*
  g++ -o prog prog.cpp -O3 -march=native \
      -std=c++17 -pedantic -Wall -Wextra -Wconversion
*/

#include <iostream>
#include <stdexcept>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#include <chrono>
#include <random>

int
get_elem_count(int argc,
               char **argv)
{
  auto elem_count=-1;
  if(argc>1)
  {
    try
    {
      elem_count=std::stoi(argv[1]);
    }
    catch(...)
    {
      // ignore
    }
  }
  return elem_count;
}

std::vector<double>
generate_sequence(int elem_count)
{
  auto gen=std::default_random_engine{std::random_device{}()};
  auto dist=std::uniform_real_distribution<double>{0.0, 1.0};
  auto sequence=std::vector<double>{};
  sequence.reserve(elem_count);
  for(auto i=0; i<elem_count; ++i)
  {
    sequence.emplace_back(dist(gen));
  }
  return sequence;
}

double
current_time()
{
  const auto now{std::chrono::system_clock::now().time_since_epoch()};
  return 1e-6*double(std::chrono::duration_cast
                     <std::chrono::microseconds>(now).count());
}

void
vector_test(const std::vector<double> &sequence,
            std::vector<double> &tested)
{
  //~~~~ consume the sequence and store values ~~~~
  tested.clear();
  for(const auto &elem: sequence)
  {
    tested.emplace_back(elem);
  }
  std::sort(begin(tested), end(tested),
    [](const auto &lhs, const auto &rhs)
    {
      return lhs>rhs;
    });
  //~~~~ make use of the sorted values ~~~~
  auto previous=1.0;
  for(const auto &elem: tested)
  {
    if(elem>previous)
    {
      throw std::runtime_error{"this is just a dummy test (never true) "
                               "in order to prevent the optimizer from "
                               "discarding all the code..."};
    }
    previous=elem;
  }
}

void
priority_queue_test(const std::vector<double> &sequence,
                    std::priority_queue<double> &tested)
{
  //~~~~ consume the sequence and store values ~~~~
  for(const auto &elem: sequence)
  {
    tested.emplace(elem);
  }
  //~~~~ make use of the sorted values ~~~~
  auto previous=1.0;
  while(!empty(tested))
  {
    const auto elem=tested.top();
    tested.pop();
    if(elem>previous)
    {
      throw std::runtime_error{"this is just a dummy test (never true) "
                               "in order to prevent the optimizer from "
                               "discarding all the code..."};
    }
    previous=elem;
  }
}

int
main(int argc,
     char **argv)
{
  const auto elem_count=get_elem_count(argc, argv);
  if(elem_count<=0)
  {
    std::cerr << "usage: " << argv[0] << " iteration_count\n";
    return 1;
  }
  const auto iteration_count=
    int(1'000'000'000.0/(elem_count*std::log(elem_count)));
  const auto generation_count=int(std::sqrt(iteration_count));
  const auto repeat_count=iteration_count/generation_count;
  auto vector_duration=0.0;
  auto priority_queue_duration=0.0;
  for(auto generation=0; generation<generation_count; ++generation)
  {
    const auto sequence=generate_sequence(elem_count);
    auto tested_vector=std::vector<double>{};
    auto tested_priority_queue=std::priority_queue<double>{};
    auto t0=0.0;
    for(auto repeat=0; repeat<repeat_count; ++repeat)
    {
      if(repeat==1) // 0 is a dry run
      {
        t0=current_time();
      }
      vector_test(sequence, tested_vector);
    }
    vector_duration+=current_time()-t0;
    for(auto repeat=0; repeat<repeat_count; ++repeat)
    {
      if(repeat==1) // 0 is a dry run
      {
        t0=current_time();
      }
      priority_queue_test(sequence, tested_priority_queue);
    }
    priority_queue_duration+=current_time()-t0;
  }
  std::cout << elem_count << " elements, "
            << generation_count*repeat_count << " iterations --> "
            << "v: "<< vector_duration << "s  "
            << "pq: "<< priority_queue_duration << "s  "
            << "(x " << priority_queue_duration/vector_duration << ")\n";
  return 0;
}