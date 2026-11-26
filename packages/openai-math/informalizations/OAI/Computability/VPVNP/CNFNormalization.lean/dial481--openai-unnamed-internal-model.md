---
{
  "module": "OAI/Computability/VPVNP/CNFNormalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CNFNormalization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CNFNormalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounding the number of clauses by the number of literals

A single empty clause rejects every assignment. Replacing an inconsistent
formula containing an empty clause by that clause alone controls its clause
count even when the input length bound counts only literal occurrences.


### `normalizeClauses`

 Keep a single empty clause when the input contains one. 

### `normalizeClauses_polynomial_bounds`

 For a family bounded in literal occurrences, both normalized size measures
are polynomially bounded. 
