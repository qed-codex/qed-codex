---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SunflowerBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SunflowerBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SunflowerBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Literal-set sunflower branching

Concrete CNF children and their semantic union, together with the absorption
invariants used by the cumulative-insertion argument. Opposite polarities are
distinct literals; no variable-disjointness premise is used.


### `Antichain`

 The antichain convention at each normalized node. 

### `clauses`

 Add a common literal-set core to each petal. 

### `childA`

 The unselected clauses are retained in each branch. 

### `eval_children_iff`

 The semantic identity holds for arbitrary petals, independently of the
sunflower's combinatorial disjointness properties. 

### `replace`

 Generic absorption replacement; a sunflower is one source of its hypotheses. 

### `no_old_subset_new`

 An inserted strict subset of an old clause has no old clause below it. 

### `inserted_survive`

 Every proposed insertion survives absorption. 

### `removed_contains_inserted`

 Every deleted old clause has a strict-subset witness among new clauses. 

### `Sunflower`

 A uniform literal-set sunflower with a nonempty core and at least two
petals. Nonemptiness of each petal is a theorem, not a field. 

### `petalFamily`

 Extract the petals by removing a known common core. 

### `Sunflower.ofClauses`

 Construct the branching data from the usual common-intersection definition
of a uniform sunflower. The pairwise hypothesis is exactly the second conjunct
of `SubexponentialSAT.Sunflower.IsSunflowerWithCore`. 

### `not_tautology_of_subset`

 Tautology-freeness is inherited by every subclause. 

### `childA_implies_parent`

 Neither normalized child introduces a satisfying assignment of its parent. 

### `literalMass`

 A finite structural measure for recursive branching; no runtime assertion. 

### `literalMass_childA_lt`

 Core replacement strictly decreases total literal occurrences. 

### `literalMass_childB_lt`

 Petal replacement strictly decreases total literal occurrences. 
