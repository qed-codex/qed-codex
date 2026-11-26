---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSmallInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSmallInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSmallInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite fallback for size-dependent subexponential parameters

The relevant cutoff is a fixed bound on the *input size*, obtained only after
proving eventual success of every layout check. The growing block threshold
must not itself be treated as a constant.

Numerical finite-maximum bounds below are separate from machine execution.
The final section reuses the already proved finite-language primitive machine;
this supplies an actual bounded-input solver, not a cost assigned to a function.


### `factor`

 Exponential factor in the precise target, using its shifted double logarithm. 

### `scale_eq_zero_iff`

 No zero-denominator convention is needed at any input size. 

### `fallback_bounded_of_eventually`

 An eventual parameter estimate supplies one fixed input-size cutoff. 

### `fallback_finite_of_eventually`

 The set of exceptional sizes, rather than a growing layout threshold, is finite. 

### `radius_ge_32_of_tail`

 The source's integer tail check already forces the required radius bound
when the point count and incidence count are nondegenerate. 

### `logCutoff_exists`

 Explicit threshold for the source's first logarithmic-domain check. 

### `goodInput_iff_cutoff`

 The source's domain test is exact even for n=0 and n=1. 

### `CheckData`

 The four natural-valued schedules inspected by the source's layout guard.
Their definitions and growth estimates are supplied by parameter construction. 

### `TailPass`

 Exact sufficient tail inequality checked by the uniform algorithm. 

### `BlockPass`

 Exact dimension check against the growing, input-dependent block threshold. 

### `Ready`

 The source's three-part guard. Its arithmetic predicates are decidable. 

### `ready_positive`

 Every division and nonempty-dimensional counting operation is reached only
on a positive-capacity, positive-dimension input. 

### `ready_radius`

 No additional R>=32 test is needed when the point and incidence counts have
been proved nondegenerate by the parameter construction. 

### `eventually_ready`

 Only the two substantive eventual growth estimates remain as hypotheses;
the logarithmic domain condition is proved outright. 

### `exists_fallback_cutoff`

 A single input-size cutoff suffices even though every component of c may grow. 

### `fixed_width_fallback_cutoff`

 The cutoff may depend on the fixed width, but is selected before n varies. 

### `actualChecks`

 Instantiate the exact checks using the selected quartic prime extension
and the source's integral expression for its block threshold. 

### `prime_requirement_le_polynomial`

 A uniform polynomial estimate for the sufficient prime-size condition. 

### `eventually_actual_prime_requirement`

 The actual prime chosen from its dyadic interval eventually dominates the
prime requirement, for every fixed polynomial incidence bound. 

### `eventually_actual_tail`

 Eventual validity of the actual tail guard is proved, not assumed, once the
incidence construction supplies its claimed fixed polynomial bound. 

### `eventually_actual_ready`

 After the independent block-fit estimate, all checks succeed eventually
for the actual selected prime and every such incidence schedule. 

### `eventually_actual_ready_of_polynomial_bound`

 All arithmetic checks hold eventually for the actual computed prime and
packing schedule. The only growth input is the independently required fixed
polynomial incidence bound, with positive incidence on the used domain. 

### `actual_fallback_cutoff`

 The fallback threshold is fixed once k and its incidence-bound constants
are fixed. It does not grow with the input size. 

### `bruteForce_le_factor`

 For a fixed exceptional-size bound, ordinary exhaustive search has a fixed
multiplicative loss relative to every target with nonnegative exponent constant. 

### `polynomial_bruteForce_le_factor`

 Input-length polynomial factors remain outside the finite maximum. 

### `finiteCoefficient`

 Exact finite maximum of normalized coefficients, including size zero. 

### `finite_polynomial_family_le_bound`

 Per-size coefficients and degrees are made uniform over the finite fallback
range; explicit input length remains arbitrary. No algorithmic bound is assumed. 

### `exists_uniform_fallback_bound`

 Finite fallback absorption keeps the chosen exponent constant exactly fixed. 

### `parsing_plus_bruteForce_le_bound`

 Additive parsing costs and exhaustive search can be absorbed together. 

### `bound_mono_coefficient_degree`

 Increasing a nonnegative target coefficient and polynomial degree enlarges
the target bound, while keeping its subexponential exponent constant. 

### `global_bound_of_finite_and_valid_bounds`

 Numerical gluing of an eventual valid-branch bound and finite exceptional
polynomial bounds. The result really uses one coefficient and one degree for
all input sizes, with the same chosen exponent constant `A`.

`T` is merely a real-valued quantity here. A caller must separately establish
that `T` bounds actual primitive execution steps. 

### `smallSolver_subexp_bound`

 An actual primitive machine for every fixed bounded-variable range. Its
finite accepted-language table was built with the exhaustive Boolean evaluator
in `FixedParameters`, separately from all numerical cost absorption above. 

### `small_log_solver_subexp_bound`

 The source's first fallback (small or zero logarithms) has an unconditional
fixed primitive solver, before any asymptotic layout estimate is invoked. 

### `exists_machine_for_fallback`

 Once the parameter checks are proved eventually, one fixed primitive
machine handles all remaining sizes. This does not compile the guard or the
large-input branch into a complete solver. 

### `actual_fallback_machine`

 A proved primitive small-input branch for the actual parameter schedule,
with a fixed finite machine chosen before the formula or its size. This is
separate from compiling the complete guarded large/small algorithm. 
