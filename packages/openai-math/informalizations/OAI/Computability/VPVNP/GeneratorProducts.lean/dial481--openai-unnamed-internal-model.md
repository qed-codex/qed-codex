---
{
  "module": "OAI/Computability/VPVNP/GeneratorProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GeneratorProducts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GeneratorProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of old and added generators in the exact extension proof

The monomials in Theorem 2.4 have arbitrarily many embedded old factors
and either one star generator or two split wires. Multiplicativity folds
all the old factors into one embedded product. The common-exponent
monomial retains both required wires with equal multiplicities.


### `fold_generatorProduct`

 Separate the finite product into its old factors and its added factors.
The two groups can have different, individually prescribed exponents. 

### `fold_generatorMonomial`

 A monomial of finite support contains every extra generator to its
prescribed power. Exponents outside its support contribute units. 

### `fold_generatorBalanced`

 If all extra generators are required, each appears exactly `e` times
in the reference monomial. 

### `fold_starMonomial`

 One star generator in an arbitrary monomial. 

### `fold_starBalanced`

 One required star generator in the reference monomial. 

### `fold_splitMonomial`

 The two split-wire multiplicities in an arbitrary monomial. 

### `fold_splitBalanced`

 The two required split wires occur with equal multiplicity in the
reference monomial, so its center can contract to the full identity. 
