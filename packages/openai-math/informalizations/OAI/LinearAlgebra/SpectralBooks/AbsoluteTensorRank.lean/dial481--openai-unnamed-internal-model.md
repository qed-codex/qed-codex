---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/AbsoluteTensorRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/AbsoluteTensorRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/AbsoluteTensorRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Asymptotic rank over all fields of a characteristic

The polynomial equations expressing a decomposition over any field extension
have a solution over the algebraic closure. Combining this specialization
with finite-extension descent gives scalar invariance without an algebraicity
hypothesis, hence characteristic invariance for matrix multiplication tensors.


### `exists_specialization`

 Specialize a finite tuple to an algebraically closed field while preserving
all polynomial equalities over its ground field. 

### `rankAtMost_of_extension_to_algClosed`

 A finite tensor defined over `F` admitting an exact rank decomposition over
`E` admits one of the same size over an algebraically closed `K` extending `F`. 

### `asymptoticRank_map_eq`

 A scalar extension of any transcendence degree preserves the asymptotic
rank of every finite three-tensor. 

### `asymptoticRank_matrixTensor_baseChange`

 All fields extending `F` give the same asymptotic rank to the matrix tensor. 

### `asymptoticRank_matrixTensor_eq_of_ringChar_eq`

 The rectangular matrix tensor's asymptotic rank depends only on the
characteristic, including characteristic zero. 

### `matrix_asymptoticRank_eq_of_charP`

 The characteristic-wise comparison in the notation `CharP F p`, with `p = 0`
allowed. 
