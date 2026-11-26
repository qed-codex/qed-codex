---
{
  "module": "OAI/Computability/VPVNP/CertificateReduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CertificateReduction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CertificateReduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reduction of the bounded certificate matrix to prime characteristic

Section 8.2 of *VP and VNP differ over every field* uses an integer matrix of
coefficient rows and the target row for the constant polynomial one. When the
target raises the rational rank, every prime avoiding a fixed nonzero maximal
minor of the augmented matrix preserves nonmembership in the row span.


### `castMatrix`

 An integer coefficient matrix over a specified ring. 

### `augment`

 Add the target coefficient row to the matrix of candidate certificates. 

### `rank_mod_le_rat`

 Reduction of an integer matrix modulo a prime cannot increase its rational rank. 

### `rank_lt_augment_iff`

 A target is outside the row span precisely when adding it raises rank. 

### `notMem_rowSpan_of_not_dvd_minor`

 The explicit good-prime test. A nonvanishing augmented minor whose order
exceeds the original rational rank obstructs row-span membership modulo `p`. 

### `natAbs_compound_le`

 The permutation expansion bounds an integer minor of order `q` by
`q! * L^q` when all entries have absolute value at most `L`. 

### `exists_bounded_good_prime`

 With at most `2^a` columns and entries bounded by `2^b`, a prime of at
most `2 * (a + clog 2 (a+b+2)) + 2` bits preserves the obstruction.
No restriction on the number of rows is needed. 

### `exists_good_prime`

 Every rational rank-raising target remains outside the certificate row span
in some prime characteristic. 

### `exists_bounded_good_prime_of_notMem`

 The bounded good-prime criterion on arbitrary finite index types, with the
rational hypothesis expressed directly as nonmembership in the row span. 
