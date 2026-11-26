---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTableInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTableInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTableInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform executable table interpolation

Every parameter in the bounds below is allowed to grow. Coefficient arithmetic,
inverse calls, syntax size, and encoded data length are kept separate from
primitive Turing-machine runtime.


### `mapWithCost`

 A measured map which evaluates each input and each tail exactly once. 

### `factorWithCost`

 One normalized linear factor. The inverse is supplied as stored data.
The two charged operations are one multiplication and one negation. 

### `basisBudget`

 Fixed polynomial in the number of labels, not a fixed-parameter constant. 

### `cacheWithCost`

 All basis rows are computed once and retained as a dense coefficient cache. 

### `Row`

 One explicitly stored row. Duplicate labels are interpreted by addition. 

### `grid`

 Explicit Cartesian enumeration by reusing the already-built shorter grid. 

### `fullRows`

 Construct the full explicit input table in exactly p^k rows. 

### `hornerExpr`

 Horner syntax with a supplied coefficient representation. 

### `tableExpr`

 The tensor Lagrange table stays factored; no multivariate expansion occurs. 

### `fullRows_eq_mvInterpolate`

 The executable complete table is exactly the previously proved tensor
Lagrange polynomial, rather than merely agreeing with it on selected inputs. 

### `inverseWithCost`

 A linear Fermat power followed by a shared finite geometric correction.
Only ring additions, subtractions and multiplications occur. 

### `integerCacheWithCost`

 Complete table-basis preprocessing, including all inverses as explicit loops. 

### `integerCacheMap`

 Transport the computed base-ring cache through a supplied coefficient map. 

### `tablePolynomial_eval₂_labels`

 The exact grid identity survives every coefficient-ring homomorphism. 

### `tableExpr_at_labels`

 In particular, a path whose value at T=0 is an integer label has the exact
original table value at T=0, after any coefficient embedding. 

### `fullRows_reindexed`

 Direct bridge from explicit finite rows to a table on an arbitrary finite
scope and arbitrary finite label type. Both equivalences are supplied data. 

### `rowCode`

 Coefficient followed by its fixed number of fixed-width integer labels. 

### `pad`

 Zero padding gives each cached polynomial a fixed number of coefficient slots. 

### `encodeTable`

 Parameters p,k,mu and the row count determine every block boundary. 
