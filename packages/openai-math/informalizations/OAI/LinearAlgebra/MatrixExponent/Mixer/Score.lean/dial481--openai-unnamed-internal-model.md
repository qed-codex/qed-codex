---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Mixer/Score.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Mixer/Score.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Mixer/Score.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary autocorrelations

The unnormalized Walsh transform doubles at each level under iteration.
It diagonalizes convolution on binary addresses. The identities only
use commutative ring operations, including in characteristic two.


### `autocorrelation`

 Two butterfly transforms and entrywise squaring compute the
autocorrelation times the number of blocks. 


# Aggregating the reset score by depth and binary difference

Only the uncentered second moments depend on the mixer. Consequently
one array, indexed by depth and by block difference, suffices to
compare all linear mixers. The arrays of the individual positions
and contacts are formed from their autocorrelations.


### `score_diff`

 The sign of the cost difference is exactly the sign of the difference
of the two tests on the aggregated array. 


# Butterfly circuits with a fixed dictionary

All arithmetic uses encoded words. One table computes the two butterfly
outputs together. A second table squares a word. The tensor entries of
both tables are zero or one in the network's ground field.


### `correlation_net`

 Quasilinear station and port count, independent of the arithmetic
of the encoded ring. 


# Exact integer autocorrelations in bounded binary words

For `2^h` inputs bounded by `2^d` choose `2(h+d)+1` bits per
word. Compute modulo that word size throughout the two transforms.
The final scaled integer is below the modulus. It can therefore be
recovered even though some intermediate operations may wrap.

