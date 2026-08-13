
"""
DAY 1 — Python for AI Engineering
Lesson: OOP, Type Hints, File Handling

DO NOT COPY THIS FILE.
Read each section. Understand it. Then write the exercises from scratch.
"""

# ============================================================
# SECTION 1: WHY OOP MATTERS IN AI ENGINEERING
# ============================================================
#
# Every major AI library is built on classes:
#   - OpenAI's client:  client = OpenAI()
#   - A LangChain chain: chain = LLMChain(llm=..., prompt=...)
#   - A Hugging Face model: model = AutoModelForCausalLM.from_pretrained(...)
#
# If you don't understand classes, you can't read or write AI code.
# That's why this is Day 1, not Day 10.

# ============================================================
# SECTION 2: CLASS — THE RIGHT DEFINITION
# ============================================================
#
# A class is a BLUEPRINT for creating OBJECTS.
# An object has:
#   - ATTRIBUTES: data it holds (e.g., model name, temperature)
#   - METHODS: things it can do (e.g., generate a response)
#
# Real-world analogy:
#   "LLM" is a class (the blueprint)
#   gpt4 = LLM(model="gpt-4") is an object (a specific instance)

class LLMConfig:
    """
    A configuration object for an LLM.
    In real AI apps, you'll see configs like this everywhere.
    """
    
    def __init__(self, model: str, temperature: float, max_tokens: int) -> None:
        # __init__ is called when you create an object.
        # 'self' refers to the specific object being created.
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    def is_creative(self) -> bool:
        """Temperature > 0.7 means more creative/random outputs."""
        return self.temperature > 0.7
    
    def summary(self) -> str:
        """Return a human-readable summary of this config."""
        mode = "creative" if self.is_creative() else "precise"
        return f"Model: {self.model} | Temp: {self.temperature} ({mode}) | Max tokens: {self.max_tokens}"
    
    def __repr__(self) -> str:
        """How Python displays this object when you print it."""
        return f"LLMConfig(model='{self.model}', temperature={self.temperature})"


# Creating objects (instances) from the class
gpt4_config = LLMConfig(model="gpt-4", temperature=0.7, max_tokens=2048)
claude_config = LLMConfig(model="claude-3-5-sonnet", temperature=0.2, max_tokens=4096)

print(gpt4_config.summary())
print(claude_config.summary())
print(gpt4_config.is_creative())   # True
print(claude_config.is_creative()) # False
print(repr(gpt4_config))


# ============================================================
# SECTION 3: INHERITANCE — EXTENDING A CLASS
# ============================================================
#
# When you use LangChain or Hugging Face, you INHERIT from their base classes.
# Example: class MyCustomLLM(BaseLLM): ...
#
# Inheritance means: "This class is a special version of that class."

class ChatConfig(LLMConfig):
    """
    A config specifically for chat models.
    Inherits everything from LLMConfig and adds more.
    """
    
    def __init__(self, model: str, temperature: float, max_tokens: int, system_prompt: str) -> None:
        # Call the parent class's __init__ first
        super().__init__(model, temperature, max_tokens)
        self.system_prompt = system_prompt  # New attribute
    
    def summary(self) -> str:
        # Override parent's method to add more info
        base = super().summary()
        return f"{base} | System: '{self.system_prompt[:30]}...'"


chat_config = ChatConfig(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=1024,
    system_prompt="You are a helpful AI assistant specializing in Python."
)
print(chat_config.summary())


# ============================================================
# SECTION 4: TYPE HINTS — WHY THEY MATTER IN PRODUCTION CODE
# ============================================================
#
# Type hints make your code readable and catch bugs early.
# In AI engineering, you'll work in teams. Untyped code is a nightmare.
#
# Without type hints:
#   def process(data, model, config):  # What are these? No idea.
#
# With type hints:
#   def process(data: list[str], model: str, config: LLMConfig) -> dict:

from typing import Optional, Union

def generate_prompt(
    user_message: str,
    system_prompt: Optional[str] = None,
    examples: Optional[list[tuple[str, str]]] = None
) -> str:
    """
    Build a complete prompt string.
    
    Args:
        user_message: The user's input.
        system_prompt: Optional system-level instructions.
        examples: Optional list of (user, assistant) example pairs.
    
    Returns:
        A formatted prompt string.
    """
    parts: list[str] = []
    
    if system_prompt:
        parts.append(f"System: {system_prompt}")
    
    if examples:
        for user_ex, assistant_ex in examples:
            parts.append(f"User: {user_ex}")
            parts.append(f"Assistant: {assistant_ex}")
    
    parts.append(f"User: {user_message}")
    parts.append("Assistant:")
    
    return "\n".join(parts)


prompt = generate_prompt(
    user_message="What is gradient descent?",
    system_prompt="You are a concise AI tutor.",
    examples=[("What is a tensor?", "A multi-dimensional array used in deep learning.")]
)
print(prompt)


# ============================================================
# SECTION 5: DATACLASSES — THE MODERN WAY TO WRITE CONFIG CLASSES
# ============================================================
#
# In real AI codebases, dataclasses are used constantly for configs.
# They auto-generate __init__, __repr__, and __eq__ for you.

from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    """Configuration for an AI model. Notice how clean this is."""
    model: str
    temperature: float = 0.7
    max_tokens: int = 2048
    top_p: float = 1.0
    stop_sequences: list[str] = field(default_factory=list)
    
    def is_valid(self) -> bool:
        """Validate the configuration."""
        return 0.0 <= self.temperature <= 2.0 and self.max_tokens > 0


config = ModelConfig(model="gpt-4o", temperature=0.5)
print(config)           # Auto-generated __repr__
print(config.is_valid()) # True


# ============================================================
# YOUR EXERCISES — DO NOT SKIP THESE
# ============================================================
#
# EXERCISE 1:
# Create a class called `EmbeddingConfig` that stores:
#   - model_name: str (e.g., "text-embedding-3-small")
#   - dimensions: int (e.g., 1536)
#   - batch_size: int (default: 100)
# Add a method `cost_per_million_tokens()` that returns a float.
# Add a __repr__ method.
# Create 2 instances and print them.

class EmbeddingConfig:

    def __init__(self, model_name: str, dimensions: int, batch_size: int = 100) -> None:
        self.model_name = model_name
        self.dimensions = dimensions
        self.batch_size = batch_size
    
    def cost_per_million_token(self) -> float :
        if self.model_name == "text-embedding-3-small":
            return 0.02
        elif self.model_name == "text-embedding-3-large":
            return 0.10
        else:
            return 0.50

    def __repr__(self) -> str:
        return f"EmbeddingConfig(model_name='{self.model_name}', dimensions={self.dimensions}, batch_size={self.batch_size})"

emb_1 = EmbeddingConfig("text-embedding-3-small", 1536, 100)
emb_2 = EmbeddingConfig("text-embedding-3-large", 768)

print(emb_1.cost_per_million_token())
print(emb_2.cost_per_million_token())



#
# EXERCISE 2:
# Create a dataclass called `RAGConfig` that stores:
#   - chunk_size: int (default: 512)
#   - chunk_overlap: int (default: 50)
#   - top_k: int (default: 5)
#   - embedding_model: str (default: "text-embedding-3-small")
# Add a method `is_overlap_valid()` that returns True if overlap < chunk_size.
#

from dataclasses import dataclass
@dataclass
class RAGConfig:
    chunk_size: int = 512
    chunk_overlap: int = 50
    top_k: int = 5
    embedding_model: str = "text-embedding-3-small"

    def is_overlap_valid(self) -> bool:
        return self.chunk_overlap < self.chunk_size 

rag1 = RAGConfig()
rag2 = RAGConfig(chunk_size=256, chunk_overlap=300)

print(rag1)
print(rag2)
print(rag1.is_overlap_valid())
print(rag2.is_overlap_valid())




# EXERCISE 3 (harder):
# Create a class `ConversationHistory` that:
#   - Has a messages: list[dict] attribute (starts empty)
#   - Has an add_message(role: str, content: str) -> None method
#   - Has a get_last_n(n: int) -> list[dict] method
#   - Has a clear() -> None method
#   - Has a __len__() method that returns number of messages
#
# WRITE THESE FROM SCRATCH. DO NOT copy. Type every character.

class ConversationHistory:
    def __init__(self)->None:
        self.messages= []
    
    def add_message(self, role: str, content: str)-> None:
        self.messages.append({"role":role, "content": content})

    def get_last_n(self, n:int)-> list[dict]:
        return self.messages[-n:]

    def clear(self)-> None:
        self.messages = []

    def __len__(self)-> int:
        return len(self.messages)

history = ConversationHistory()
history.add_message("User", "Hi kaise ho?")
history.add_message("Assistant", "Me theek hu tum batao")
history.add_message("USer", "kuch nahi")
print(history.get_last_n(2))
print(len(history))


    
    