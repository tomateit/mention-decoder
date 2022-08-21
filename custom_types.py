from dataclasses import dataclass
@dataclass
class Sample:
    text: str
    span: tuple[int, int]
    ent: str
    
    def from_dict(d) -> "Sample":
        return Sample(
            text=d["text"],
            span=tuple(d["span"]),
            ent=d["ent"]
        )
