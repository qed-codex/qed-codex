---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Seam.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Seam.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Seam.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Scaling, restriction and change of coefficients for pairing sums 

### `wick_scale_rows`

 Every generator occurs exactly once in each Wick monomial. 


# Number of states at bounded energy

Energy is doubled. Distinct modes give a finite subset of a rectangle.
Bounding the generating function of its powerset avoids infinite products.


### `sum_weight`

 The exponential weights for one species are bounded by a telescoping sum. 

### `card_levelLE`

 A uniform dimension bound for the direct sum through doubled energy `e`. 


# Interleaving copies of one level

Put the modes of each copy in their own residue class. Reversing the
class assignment makes the two total energies add to twice the target.
Keeping the lower one and one orientation bit is an injective encoding.


### `interleave_level`

 Amplification with a loss polynomial in the target energy. 


# Fixed-energy codes for station bits

For each bit use either the inner or outer pair of four consecutive modes.
The two choices have equal energy. This gives a quadratic energy bound at
a single integer level without partition asymptotics.


### `bitCode`

 An explicit injection of `n` bits into a single-species level of
physical energy `4n²` (doubled energy `8n²`). 


# Weighted input and output positions for two-site fusion

At doubled energies `e,g` the positions have total weight
`√e + √g`. A slot of weight `t` can be isolated with a test
of doubled energy at most `(√e + √g) * t + 1`.


### `slots`

 Input in wedge order, output in dual order. 


# Sharp common growth rate for one-species levels

The supremum of the normalized log dimensions is finite and positive.
Interleaving a fixed level approaching this supremum works at every
sufficiently large target width, with only logarithmic loss.


### `entropy_attained`

 One level below any sufficiently large quadratic cutoff nearly attains
the common log-dimension bound at the scale of the cutoff. 


# Integral tests for the two-site fusion map

The test with parameters `a,d` represents the Laurent polynomial
`X^(-a-1) (1-X⁻¹)^d`. Its leading positions at zero and one have
indices `a` and `d` respectively.


### `test_pivot`

 At equal or smaller weight only the designated slot survives. 


# Transposition at a seam

Evaluate fusion in the ordinary wedge basis by placing the output modes
last, in reverse order. Inversion negates each pairing. Reversing the
entire Wick list then cancels the signs pair by pair. This gives a single
integral lowering operator, with scalar one in every characteristic.


### `fusion`

 Matrix entry of the two-site fusion at offsets zero and one.
Contractions to the output block are the two translation coefficients.
Its reversed order gives the ordinary dual wedge pairing. 

### `entry`

 Matrix coefficient with a superposition of middle states. 

### `seam`

 The same operator transposes every fusion matrix. Each output of a
basis input preserves exterior degree and weakly lowers energy. 

### `vac`

 The empty wedge is the only state at zero energy. 
