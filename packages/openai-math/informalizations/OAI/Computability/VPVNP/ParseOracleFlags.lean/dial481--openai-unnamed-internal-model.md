---
{
  "module": "OAI/Computability/VPVNP/ParseOracleFlags.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleFlags.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleFlags.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed flag table for the integer label coefficient oracle

In §8.1 each coefficient of `Bₓ` counts ordered parses with the requested leaves
and production multiplicities. The same incidence clauses and the same two columns
of event tags work for every word `x` and every nominated exponent vector.


### `tagUnit`

 One unit of multiplicity for a tag, or zero for an absent tag. 

### `tallyFlags`

 Count occurrences by scanning the selected coordinates of a single tag column. 

### `tallyFlags_apply`

 At each coordinate the tally is the number of selected flags carrying that tag. 

### `ParseEvent.grammarLabel`

 Production label of an event in the finite rectangular table. A binary event
outside the degree or split range has no label. 

### `ParseOracleMetadata`

 The fixed advice used for the flag count. The two tag columns depend only on
the candidate event. The clauses additionally fix the root layer and state. 

### `ParseOracleMetadata.clauses`

 The fixed CNF constraints on candidate event flags used to check parse incidence. 

### `ParseOracleMetadata.terminal`

 The optional terminal-variable tag counted when the flag at this address is selected. 

### `ParseOracleMetadata.label`

 The optional grammar production label counted when the flag at this address is selected. 

### `ParseOracleMetadata.Accepts`

 Incidence plus the two queried multiplicities. No auxiliary Boolean witnesses
are introduced by the two counts. 

### `parseOracleMetadata`

 Enumerate candidate events and attach their terminal and production tags, with incidence
clauses rooted at offset zero, layer `d` and state `h`. 

### `coeff_labelQuery_eq_flagCount`

 The integer coefficient equals the count of passing flag words, with one such
word for each matching ordered parse. The metadata are fixed independently of both
arguments of the oracle, `x` and `e`. 
