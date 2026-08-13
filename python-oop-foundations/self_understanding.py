# self_demo.py — Run this to understand self

# ============================================================
# PART 1: Standalone function — no self needed
# ============================================================

def add(a, b):
    return a + b

print(add(2, 3))   # 5 — works fine, no object needed


# ============================================================
# PART 2: What if cost depends on the model?
# ============================================================
# Different models have different costs:
#   text-embedding-3-small  → $0.02 per million tokens
#   text-embedding-ada-002  → $0.10 per million tokens
#   custom-model            → $0.50 per million tokens
#
# Now the cost is NOT fixed — it depends on which model the object is using.
# How does the method know WHICH model? It needs to read self.model_name.

class EmbeddingConfig:

    def __init__(self, model_name: str, dimensions: int, batch_size: int = 100) -> None:
        self.model_name = model_name
        self.dimensions = dimensions
        self.batch_size = batch_size

    def cost_per_million_tokens(self) -> float:
        # self.model_name — reading THIS object's model name
        if self.model_name == "text-embedding-3-small":
            return 0.02
        elif self.model_name == "text-embedding-ada-002":
            return 0.10
        else:
            return 0.50

    def __repr__(self) -> str:
        return f"EmbeddingConfig(model='{self.model_name}', dims={self.dimensions})"


# Create TWO different objects
emb_1 = EmbeddingConfig("text-embedding-3-small", 1536)
emb_2 = EmbeddingConfig("text-embedding-ada-002", 768)
emb_3 = EmbeddingConfig("custom-model", 512)

# Same method — different answers for different objects
print(emb_1.cost_per_million_tokens())   # 0.02
print(emb_2.cost_per_million_tokens())   # 0.10
print(emb_3.cost_per_million_tokens())   # 0.50

# WITHOUT self, how would cost_per_million_tokens() know which model to check?
# It can't. It would have no access to model_name.
# That's why self exists.
