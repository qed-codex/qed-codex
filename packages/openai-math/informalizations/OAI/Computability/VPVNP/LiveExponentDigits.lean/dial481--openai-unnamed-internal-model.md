---
{
  "module": "OAI/Computability/VPVNP/LiveExponentDigits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentDigits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentDigits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking a running exponent one bit at a time

In the first half of the live chain an increment fits in one RAM word, while
the incoming and outgoing exponents may occupy many words. A digit call
checks the low bit of the sum and passes its quotient by two to the next
digit. Requiring zero final carry checks ordinary natural-number addition.


### `total`

 The carry and the low input bit of one digit. 

### `Checks`

 Each digit must match the outgoing bit. The final digit's carry must vanish. 

### `checks_iff`

 The checks enforce the full-width equation including overflow. 

### `checks_words`

 Specialization to the actual little-endian cut encoding. 

### `carry_le`

 Even with a long binary input exponent, the carry never grows above the
larger of the initial increment and one. 
