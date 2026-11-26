---
{
  "module": "OAI/Computability/VPVNP/StarContraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarContraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarContraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transport of a center covector

For the extension in Theorem 2.4, a covector on the output of a restriction
pulls back through the matrix at the new party. The matrices at the old
parties act after this contraction. Direct sums split the pulled-back
covector into its two coordinate blocks. An embedded old tensor has a
singleton center basis, so it factors through an arbitrary contraction.


### `pullCovector`

 The center covector pulled back through a local restriction matrix. 

### `sum_withCenter`

 Split the center index out of a sum over all local basis tuples. 

### `contractCenter_applyLocal`

 The matrix at the center acts on its covector, and all other matrices act
on the resulting old-party array. 

### `contractCenter_restricts`

 Every contraction of the demand tensor is obtained by restricting a
contraction of the supply tensor. The pulled-back covector can be entangled
across all factors at the center. 

### `contractCenter_directSum`

 Each coordinate block of the center covector contracts its own summand.
The old-party bases still form a direct sum. 

### `contractCenter_restricted_directSum`

 The old-party maps after restricting an extended direct sum act on the
contracted branches separately, with ordinary addition of their output arrays. 

### `restricts_embedOld_contractCenter`

 An extended tensor can supply any center contraction with the trivial leg
restored. This lets an extending spectral point bound the old spectral value
of every contraction. 

### `embedOld_restricts`

 Adding a trivial party preserves local restriction. 

### `embedOld_product_mutual`

 Parallel products of embedded old tensors differ from the embedded
product only by the canonical bijection of their singleton center bases. 

### `contractCenter_embedOld_one`

 Evaluating the embedded singleton leg at one returns the old tensor. 

### `restricts_contractCenter_embedOld`

 A scalar multiple of an old tensor is a local restriction: one old
party absorbs the scalar into its identity matrix. 

### `contractCenter_old_product`

 A general covector on the center leg of an old tensor times an extended
tensor leaves the old tensor intact. 
