---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rounds/Contraction/Access.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Contraction/Access.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Contraction/Access.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Retaining station identities when reducing a raw diagram 

### `Raw`

 Data and size bounds for a diagram that may have loops or scalar stations. 

### `reduced`

 Contract loops and discard scalar stations. A surviving station is indexed
by its original name together with a proof of positive residual arity. 

### `eval_reduced`

 The discarded scalar factor is allowed to vanish. 

### `input_of_diagram`

 Prepare an input without adding stations. Self-loops contribute
to their own tables, and all scalar-only stations contribute one
common factor. Every exposed wire stays in its original cell. 

 # Preparing the parallel bundles for local concentration 

### `packetize`

 Pad each nonempty ordered bundle by zero bits. This retains the
original stations and exterior ports. Doubling the width scale and
multiplying the mass budget by 101 pays for the extra bits. 

 # Extending the geometric concentration estimates to arbitrary scales 

### `floor_units`

 Taking an integral quotient loses at most a factor of two. 

### `LocalLaw.arbitrary`

 The geometric expansion for all sufficiently large integral D.
The positive bundle floor is at least `T / D^(2*C+1)`. 

 # Returning to the arity scale before bundle padding 

 # The total frozen arity in a concentration summand 


# Common record format for a family of round states

Different states may have different diagrams. A stage acts on their
encodings, allowing the controller to inspect the short records and
carry the exposed bits independently.


### `Neutral`

 Scalar-only stations have had their entries pulled into the branch
weight. This permits discarding them when packing live atoms. 


# An encoded contraction with a frozen border

Physical load and the exponent on the full degree are fixed before
choosing the degree of the input graph. Circuit exponents may depend
on this degree. The dependence of the new label width on the old
width is linear, so successive rounds can reuse the labels.


 # Shorter payloads may use a padded tag above the price threshold 

 # The common grouping for a layer of boards 

 # A snapshot of the local inputs after grouping a layer 

 # A grouped input with the original one-step host graph marked 
