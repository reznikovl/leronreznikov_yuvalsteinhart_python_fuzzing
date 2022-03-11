from utils import type_combos
from datetime import datetime

beg = datetime.now()

for i in type_combos(5):
    continue

end = datetime.now()
print(end - beg)