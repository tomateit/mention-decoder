import json
from pathlib import Path

import torch

from custom_types import Sample


class DataIterator():
    memory = []
    
    def __init__(self, file_locations):
        self.file_locations = file_locations
        
    def __next__(self):
        if not self.memory:
            if not self.file_locations:
                raise StopIteration()
            file_path = self.file_locations.pop()
            self.memory = json.loads(file_path.read_text())
            
            
        sample = self.memory.pop()
        sample = Sample.from_dict(sample)
        return sample

class IterableJsonDataset(torch.utils.data.IterableDataset):
    """
    Takes a pointer to directory with json files of
    dicts like
    Sample(text:str, ent: str, span: [int, int])
    dataclass form
    """
    
    file_locations = []
    
    def __init__(self, data_dir: Path):
        super().__init__()
        self.data_dir = data_dir
        self.file_locations = list(data_dir.glob("*.json"))
        
    def __iter__(self):
        return DataIterator(self.file_locations)