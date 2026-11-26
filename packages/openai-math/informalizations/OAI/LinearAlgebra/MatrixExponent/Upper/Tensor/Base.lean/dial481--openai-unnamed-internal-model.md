---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Base.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Base.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Base.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete finite tensors and mutual restriction

Representatives use natural-number dimensions, so the quotient is a small type.
The relation is witnessed by the three actual local coefficient matrices. In
particular, no rank or restriction oracle occurs in this definition.


### `Restricts`

 `Restricts A B` means that the source `A` restricts to the target `B`. 

### `TensorRep`

 A finite coefficient tensor with an explicit dimension on every leg. 

### `ofTensor`

 Encode arbitrary finite coordinates by their canonical finite enumeration. 

### `Equivalent`

 Mutual actual restriction, allowing unused or zero coordinates. 

### `TensorClass`

 The actual finite-tensor restriction quotient of the paper. 
