from mlbf import MLBF

mlbf = MLBF(1000000, 4)
mlbf.insert(["user123_email", "user123_phone"])
print(mlbf.query("user123_email"))  # True
print(mlbf.query("random_key"))  # False (probably)