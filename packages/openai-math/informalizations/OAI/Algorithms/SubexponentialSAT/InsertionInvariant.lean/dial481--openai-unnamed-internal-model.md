---
{
  "module": "OAI/Algorithms/SubexponentialSAT/InsertionInvariant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/InsertionInvariant.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/InsertionInvariant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degree bounds for live inserted clauses

The state remembers only the still-live clauses inserted on a branch.  Initial
clauses may have arbitrary degree.  A batch inserts at most one clause per
literal, and every inserted clause is shorter than the selected branching width.
A concrete finite trace preserves the degree bound whenever the minimum-width
rule supplies the smaller-width bound for the full parent formula.


### `widthLiteralDegree`

 Number of clauses of exactly width `j` containing the literal `a`. 

### `OnePerLiteral`

 At most one clause in the batch contains any given literal. 

### `State`

 The remembered clauses are an actual subfamily of the current formula. 

### `initial`

 Initial clauses are deliberately not marked as inserted. 

### `update`

 Insert a batch and retain exactly the clauses surviving into `G`. 

### `BatchStep`

 A batch replacement followed by deletion/absorption. 

### `PreInsertionBound`

 The bound supplied before a branch at `d` by choosing minimum width. 

### `DegreeInvariant`

 Only live inserted clauses, not arbitrary initial clauses, are bounded. 

### `widthLiteralDegree_one`

 Distinct unit clauses cannot contain the same literal. 

### `onePerLiteral_of_pairwiseDisjoint`

 In child B, disjoint petals give the one-per-literal batch property. 

### `degreeInvariant_of_tracked_subset`

 Deleting clauses can never increase a width-specific literal degree. 

### `initial_degreeInvariant`

 The empty tracked family satisfies the bound even for a dense initial CNF. 

### `BatchStep.inserted_degree_zero`

 No inserted clause has width as large as the selected width. 

### `BatchStep.preserves_degreeInvariant`

 One actual batch step preserves the insertion degree invariant. 

### `Trace`

 A finite trace records concrete batches and all intermediate finite states. 

### `Trace.preserves_degreeInvariant`

 The invariant is propagated by induction over actual branching traces. 

### `Trace.tracked_degree_le`

 Appendix A.2's degree bound, for every state reachable from an arbitrary CNF. 

### `Trace.tracked_filter_card_le`

 Filter-form interface for the removal-capacity argument. 

### `BatchStep.tracked_eq_survivors_union`

 When every batch member survives absorption, tracking has the usual form. 

### `CNFState`

 Specialization of the concrete state syntax to the SAT module's literals. 

### `thresholdDegreeBound`

 The paper's `L_j`; at widths zero and one this expression is one. 

### `MinimumWidth`

 Choosing minimum width excludes the stipulated sunflower at every smaller
width where the branching rule is defined. 

### `minimumWidth_preInsertionBound`

 The elementary sunflower theorem discharges the pre-insertion hypothesis.
The zero- and one-width cases use the concrete finite-set facts above. 

### `MinimumWidthTrace`

 A trace justified by the actual no-smaller-sunflower condition. 

### `MinimumWidthTrace.toTrace`

 Convert minimum-width combinatorics to the bounds used by the invariant. 

### `MinimumWidthTrace.tracked_degree_le`

 The invariant with `L_j` derived from the actual sunflower thresholds. 

### `MinimumWidthTrace.tracked_filter_card_le`

 Direct filter-form statement, for charging a removed tracked clause. 

### `coreChild`

 The state produced by the actual core child, including absorption. 

### `petalChild`

 The state produced by the actual simultaneous-petal child. 

### `coreBatchStep`

 The concrete core child satisfies every generic batch-step obligation. 

### `petalBatchStep`

 Disjoint petals meet the batch condition even when all are inserted at once. 

### `coreChild_tracked`

 Core insertions survive absorption under the maintained antichain condition. 

### `petalChild_tracked`

 All petals survive absorption, justifying a batch of their full cardinality. 

### `SunflowerTrace`

 An actual branch trace: every chosen sunflower occurs in the parent, has
exactly the prescribed number of petals, and has minimum eligible width. 

### `SunflowerTrace.toMinimumWidthTrace`

 The generic invariant applies to the literal-set branching algorithm. 

### `SunflowerTrace.antichain`

 Absorption preserves the antichain convention throughout actual traces. 

### `SunflowerTrace.tracked_filter_card_le`

 The Appendix A.2 invariant along actual normalized sunflower branches,
without assuming a bound on the initial formula's density. 
