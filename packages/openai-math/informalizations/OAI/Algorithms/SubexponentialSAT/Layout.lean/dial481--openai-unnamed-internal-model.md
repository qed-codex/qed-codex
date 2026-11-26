---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Layout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Assembly of interpolation layouts

This module constructs the finite extension and records concrete universal-block
and packing data used in the global layout assembly. A universal-block interface
is not itself asserted to exist without the spectral and support construction.


### `Extension`

 The actual degree-h finite extension used by the construction. 

### `extensionNodes`

 Enumerate all nonzero extension elements, not an arbitrary selection. 

### `extensionNode`

 The evaluation map consists of pairwise distinct nonzero nodes. 

### `UniversalBlock`

 Concrete universal-block data to be furnished by the matrix construction.
The subspaces are over the base field; the row polynomials use the extension. 

### `twice_card_side`

 The cardinality of either universal side is half of the block size,
expressed without division or a positivity side condition. 

### `packed_dimension_lower`

 Combining the universal-side estimate with three-quarter coverage gives
at least one quarter of the global coordinates in each free subspace. 

### `embeddedRow`

 Embed one block row by zero outside that block. 

### `blockEmbedding`

 One block of an injective packing. 

### `assembledRow`

 Packed vertices use their block row; uncovered vertices use the constant
coordinate selector. The construction does not require entire factors in a block. 

### `universalBlockOfRank`

 Bundle the actual matrix, actual common fixed subspaces and actual
interpolated rows. The sole remaining local hypothesis is the explicit rank
bound for the concrete projector matrix. 

### `embeddedRow_eval`

 Evaluating embedded polynomial coefficients is the same as embedding the
already evaluated row. 

### `embeddedRow_pairing`

 Pair a block polynomial row with an arbitrary full-coordinate vector. 

### `fromBlocks`

 Assemble every field of the genuine layout interface from a concrete
universal block and a compatible three-quarter packing. No global row-path,
annihilation, support or dimension condition is assumed. 

### `exists_of_universalBlock`

 The balancing and packing steps require only bounded incidence and the
explicit fixed threshold. In particular no type-distribution assumption remains. 

### `Construction`

 A single finite construction is fixed before either the coordinate count
or the factor pattern varies. Its field is an actual finite Galois extension. 

### `layout_exists`

 The same finite construction works for every sufficiently large bounded
pattern. The coordinate and factor index types are arbitrary finite types. 

### `two_ne_zero`

 Odd prime characteristic makes the normalization by two legitimate. 

### `constructionOfParameters`

 With numerical parameters fixed, the explicit concrete-matrix rank bound
completes the finite construction. All other block and global properties are
already theorems above. 

### `exists_construction`

 Unconditional existence of the complete finite interpolation gadget.
This combines finite-field construction, binomial interpolation, the actual
matrix spectrum and its integer tail bound. No layout or rank assumption remains. 

### `interpolation_layout_exists`

 Mathematical existence part of Lemma 3.1, with the quantifier order explicit:
constants are fixed before D, the number of factors, or any bounded pattern.

This theorem asserts the full finite layout properties. A polynomial bit-time
implementation of this construction is a separate, unproved obligation. 

### `exists_blocks_for_computedAssignment`

 The actual local-expectation program supplies the type labels for the
packing theorem. No finite-averaging choice of an assignment is used here.
The packing itself is still supplied by its proved finite existence theorem. 

### `exists_layout_with_computed_words`

 Replace the abstract assignment-existence step in the layout construction
by the exact output of the executable local conditional-expectation program.
The returned layout's factor words are that program's output, propositionally,
not merely some other assignment with a matching deviation bound.

This does not claim the rest of the layout has an executable representation:
block enumeration and the finite-field/basis data remain separate obligations. 

### `Construction.layout_exists_computed`

 The unconditional finite construction also accepts the program's specific
word assignment. Only the explicit executable-input representations are supplied. 
