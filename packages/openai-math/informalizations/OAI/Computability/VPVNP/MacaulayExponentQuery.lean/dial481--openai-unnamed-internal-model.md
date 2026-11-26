---
{
  "module": "OAI/Computability/VPVNP/MacaulayExponentQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bit-stack queries for the exponents in Macaulay entries

After ordinal lookup, the low radix block of each raw key contains the
actual exponents in variable order. The common word width accommodates both
index scans, the shift by one label, and the scaled source digit. Division
by the monomial, powered-row equality, and the requested exponent difference
are recovered in the original label order.


### `entryWidth`

 Register width for the two index scans and the shifted exponent comparison. 

### `params`

 Set the source and column radices to their degree bounds plus one and install the scaling,
marked coordinate and requested coordinate. 

### `exponentBlock`

 Remove the degree digit of a raw graded monomial address. 

### `shifted`

 The exponent at variable i after multiplying by the marked variable and raising the
resulting monomial to the indicated power. 

### `row_run`

 The fixed control returns the divisibility and equality tests in all
labels, and the difference exponent of any single requested label. 

### `entryWidth_polynomial`

 The width of each register in the scalar entry tests is polynomially
bounded for polynomially many labels and polynomial-bit degree and scale inputs. 
