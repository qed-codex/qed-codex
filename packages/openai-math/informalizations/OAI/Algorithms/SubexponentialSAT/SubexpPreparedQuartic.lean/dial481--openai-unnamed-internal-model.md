---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPreparedQuartic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPreparedQuartic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPreparedQuartic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quartic operations with a stored modulus

The modulus is input data. None of the operations in this file computes
`p^mu`, its bit expansion, or an irreducible polynomial. Setup is separate.


### `Modulus`

 Prepared bytes together with their mathematical interpretation. 

### `canonicalModulus`

 A specification-level constructor. The counted setup implementation can
instead pass its computed bytes directly to the `Modulus` constructor. 

### `prepareModulus`

 Actual setup computes the modulus from the supplied prime word using
binary multiplication. Natural exponentiation appears only in the proof. 

### `literalWordRun`

 The same explicit traced copying/padding routine prepares literal words.
Its input is a fixed literal list, never a natural-number residue conversion. 

### `prepareZero`

 Four literal-word constructions, including all copying/padding events. 

### `zeroWord`

 A stored zero word avoids computing any residue representation inside
the negation callback. 

### `prepareReduction`

 Prepare the reduction cache by an actual binary negation of the four
already encoded coefficients. Its setup cost is charged once. 
