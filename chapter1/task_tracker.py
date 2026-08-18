from dataclasses import dataclass, field
 
 
@dataclass
class Task:
    title: str
    priority: int = 1
    tags: list = field(default_factory=list)   # fixed: fresh list per instance
 
 
def main():
    t1 = Task(title="Write report")
    t2 = Task(title="Fix bug", priority=2)
    print(t1)
    print(t2)
 
 
if __name__ == "__main__":
    main()
 