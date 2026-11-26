---
{
  "module": "OAI/Computability/VPVNP/PerronBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bit lengths of Perron degrees and Macaulay dimensions

The coefficient count for a Perron relation permits a degree that depends on
the number of variables. Its binary logarithm remains polynomially bounded
when the variable count and the input-degree logarithm are polynomially
bounded. The same holds for the dimensions of the resulting Macaulay matrix.


### `perronSimplexBound_le_paper_envelope`

 The multiplier degree allowance obtained by substituting in a Perron
relation fits the paper's bound `H(d,t) = (2d)^(4(t+2))`. 

### `polynomiallyBounded_clog_perronSimplexBound`

 The Perron degree has polynomial bit length even for input degrees of
polynomial bit length. 

### `polynomiallyBounded_clog_paperBound`

 The paper's effective Nullstellensatz multiplier allowance has polynomial bit length. 

### `polynomiallyBounded_clog_boundedMonomial`

 Bit length of the actual index set of columns in a bounded coefficient matrix. 

### `polynomiallyBounded_clog_macaulayDimensions`

 For a Macaulay matrix formed from a certificate of multiplier degree `H`
and equations of degree `d`, both index sets have polynomial bit length. 

### `polynomiallyBounded_good_prime_bits`

 The bit-length allowance for the prime in the characteristic-zero reduction
stays polynomial even if the coefficients have singly exponential bit length. 
