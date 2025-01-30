'''
    Given a pathname, return the shortest equivalent pathname.
'''

def pathname(path: str) -> str:
    if not path:
        raise ValueError("Empty path is not a valid path")  
    path_names = [] # Stack
    if path[0] == "/":
        path_names.append("/")
    for token in (token for token in path.split("/") if token not in [".", ""]):
        if token == "..":
            if not path_names or path_names[-1] == "..":
                path_names.append(token)
            else:
                if path_names[-1] == "/":
                    raise ValueError("Path error.")
                path_names.pop()
        else:
            path_names.append(token)
    result = "/".join(path_names)
    return result[result.startswith("//"):]

print(pathname("abc//./../../names/lyte/../nyte"))