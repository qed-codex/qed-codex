---
{
  "module": "OAI/Computability/VPVNP/ExactOneClauses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneClauses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneClauses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact-one clauses for a CNF verifier

Each clause selects one literal occurrence. Its selector requires that occurrence
to be true and all earlier occurrences to be false. Each implication uses one
filler bit in an exact-one triple. Pairs outside the triangular part of the table
receive a singleton constraint fixing their filler to false.


### `Holds`

 An exact-one constraint counts literal occurrences, including repetitions. 

### `Occ`

 A literal occurrence identified by its clause and its position within that clause. 

### `PairOcc`

 An ordered pair of literal occurrences in the same clause, including pairs with equal
positions. 

### `Slot`

 Variables of the exact-one encoding, partitioned into original data bits, occurrence
selectors, and pair fillers. 

### `width`

 Total number of Boolean variables in the exact-one encoding of the formula. 

### `index`

 Number the three kinds of exact-one variables by finite ordinals. 

### `data`

 Variable index in the exact-one encoding that carries the original Boolean variable `v`. 

### `selector`

 Variable index marking occurrence `i` as the selected literal in clause `c`. 

### `filler`

 Variable index for the filler attached to ordered positions `i,j` in clause `c`. 

### `original`

 Recover the original assignment from an assignment to the enlarged exact-one variable set. 

### `needed`

 Bit required by selector `i` when testing occurrence `j ≤ i`. 

### `selectorClause`

 Clause of positive occurrence selectors requiring exactly one selected position in the
original clause. 

### `pairClause`

 Exact-one constraint comparing a candidate selector at `i` with occurrence `j`, with a
filler bit making the choice canonical. 

### `rows`

 The selector clause and all ordered-pair constraints for one clause of the original
formula. 

### `augment`

 Polynomial-size exact-one CNF with original, selector and filler variables. 

### `selectedOnce`

 Exactly one occurrence selector in clause `c` is true under assignment `x`. 

### `holds_augment_iff`

 Exact-one satisfaction determines one selector per clause, forces the tested
literal or its negation when that selector is true, and determines every filler bit. 
