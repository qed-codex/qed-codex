---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of ExactExponent.lean: how the three final theorems are assembled

**This file of 65 lines is the module that the source's Comparator configuration names as the solution. It contains proofs of three theorems with the names and the wording of the Comparator statement: the square exponent $9/4$, the dual exponent $1/2$ and the formula for rectangular formats. Each proof is a few lines long and cites results from other files. The value $9/4$ and the rectangular formula over fields enter through one imported theorem, `omega_eq_and_rigidity`. The comparisons between models of computation, the cyclic symmetry and the upper bound over rings are separate imported results, proved in files that do not import that theorem.** What this file adds is bookkeeping: which model, which order of the three dimensions, what to do with negative weights, and the sorted form of the formula. The writer has not built the project.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## Two copies of the definitions

This file does not import the statement file. Its theorems are about definitions with the same names and the same wording, declared again inside the proof's own files. [The copy of `formalOmega` that this file uses](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ArithmeticExponent.lean#L22-L30) That the two sets of definitions agree is what Comparator is meant to check.

## Three models of computation

The proofs move between three models. All three count one unit per arithmetic operation and allow results to be reused. They differ in whether division is allowed and in how a computation is recorded.

1. **The formal model** of the Comparator statement. Programs fill numbered registers using addition, subtraction and multiplication. There is no division. Correctness is an identity of polynomials. Its exponent is `formalOmega F w12 w23 w31`. [Statement file, lines 96–104](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L96-L104)
2. **The integral model.** It is also division-free and also asks for polynomial identities, and it is defined over any commutative ring. It records the set of polynomials available so far: the constants and the inputs at the start, then one new sum, difference or product per step. Its exponent is `Integral.exponent A a b c`, with the dimensions ordered as rows, columns, inner dimension. [Integral/Model.lean, lines 16–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Model.lean#L16-L36)
3. **The rational model.** Computations take place in the field of rational functions in the input variables, and dividing one available value by another is a permitted step when the divisor is not zero. Its exponents are `omega F` for square matrices and `Rectangle.exponent F a b c` in general, again ordered as rows, columns, inner dimension. [RationalCircuits.lean, lines 30–44](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/RationalCircuits.lean#L30-L44) · [Rectangle/Model.lean, lines 26–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean#L26-L36)

## The square exponent

The proof chains two equalities. [Lines 10–12](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L10-L12)

- `formalOmega F 1 1 1 = omega F`. The formal model and the rational model have the same square exponent, so allowing division does not lower it. The cited theorem compares both exponents with the tensor ranks of the square matrix multiplication tensors. [formalOmega_square_eq_omega](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/SquareRankModel.lean#L42-L52)
- `omega F = 9/4`. [omega_eq](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/FieldFormula.lean#L11-L13)

The number $9/4$ is therefore established in the rational model and carried over.

## The dual exponent

The proof uses both halves of one imported theorem, `omega_eq_and_rigidity`: the equality `omega F = 9/4` and the property `Rectangle.Rigidity F`. [Lines 14–27](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L14-L27) · [omega_eq_and_rigidity](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/FieldFormula.lean#L8-L9)

It first shows that the dual exponent of the Comparator statement equals the internal quantity `Rectangle.dual F 1 1`. In general `Rectangle.dual F a b` is the supremum of the $c$ between $0$ and $\min(a, b)$ for which the rational exponent with rows $a$, columns $b$ and inner dimension $c$ equals $a + b$. [Rectangle/Model.lean, lines 38–39](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean#L38-L39)

The two definitions look at different shapes. The Comparator statement multiplies a matrix with $\lceil N^{t} \rceil$ rows and $N$ columns by an $N \times N$ matrix. The internal definition multiplies an $N \times \lceil N^{t} \rceil$ matrix by an $\lceil N^{t} \rceil \times N$ matrix. For each $t \in [0, 1]$ the proof joins them with three rewrites:

1. `formalOmega F 1 1 t = Integral.exponent F t 1 1`. The formal and integral models have the same exponents once the three weights are read in the opposite order. [formalOmega_eq_integral](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RectangularCircuitModel.lean#L125-L143)
2. `Integral.exponent F t 1 1 = Rectangle.exponent F t 1 1`. Over a field, and for nonnegative weights, the division-free and rational models have the same exponent. [Integral.agreement](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/UpperBound.lean#L360-L371)
3. `Rectangle.exponent F t 1 1 = Rectangle.exponent F 1 1 t`. For nonnegative weights, rotating the three dimensions cyclically does not change the exponent. [Rectangle.cycle](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/FieldExtension.lean#L99-L105)

The value then comes from `Rectangle.dual_square`, the case $a = b = 1$ of the formula `dual F a b = a b / (a + b)` for positive $a$ and $b$. Both take rigidity and the square value $9/4$ as hypotheses. [Rectangle/Dual.lean, lines 180–186](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Dual.lean#L180-L186)

## The rectangular formula

Three rewrites and one private lemma. [Lines 48–61](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L48-L61)

1. **Negative weights.** `formalOmega F a b c` is unchanged when each weight is replaced by its maximum with $0$. For $N \ge 1$ a side of weight $w \le 0$ has length $1$, the same as a side of weight $0$, so the two families of formats are identical. [formalOmega_max_zero and its helper](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RectangularCircuitModel.lean#L145-L170)
2. **To the integral model**, by the same theorem as in step 1 of the dual exponent.
3. **The formula over rings.** For every nonzero commutative ring $A$ and nonnegative weights, `Integral.exponent A a b c = Rectangle.U a b c`. Here it is applied with $A = F$. [Integral.exponent_eq](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/RingFormula.lean#L8-L11) Its proof has two halves. The upper bound holds over every commutative ring and comes from rank decompositions with integer coefficients. [arithmetic_upper](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/UpperBound.lean#L342-L350) The lower bound maps a circuit over $A$ to the quotient of $A$ by a maximal ideal and applies the rational-model formula over that field. [of_fields](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/UpperBound.lean#L373-L379) · [Rectangle.exponent_eq](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/FieldFormula.lean#L18-L22)
4. **Sorting.** The function `U` is defined by cases on which of its arguments is smallest. [Rectangle/Model.lean, lines 46–55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean#L46-L55) The Comparator statement writes the same quantity with a maximum, a minimum and the middle value. The private lemma `benchmark_sorted` proves that the two expressions are equal. [Lines 29–46](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L29-L46)

## Where the number 9/4 comes from

Not from this file. Each of the three theorems uses `omega_eq_and_rigidity`, which states for every field $F$ that `omega F = 9/4` and that `Rectangle.Rigidity F` holds.

Rigidity is the source's own name for a property defined in the lines cited below. It should not be read as matrix rigidity in Valiant's sense. It is an either-or statement about positive weights. Either the rational exponent equals `U a b c` for all positive $a$, $b$, $c$. Or it is strictly smaller than `U a b c` at every positive shape where `U a b c` exceeds all three sums of two weights. [Rectangle/Model.lean, lines 57–62](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Model.lean#L57-L62) Together with the square value $9/4$ it gives the formula for all nonnegative shapes. [all_shapes](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Dual.lean#L147-L152)

The proof of `omega_eq_and_rigidity` is one line. It applies `contact_of_installations` to `Rounds.installable` at the prime fields $\mathbb{Z}/p$. [contact_of_installations](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Realization.lean#L15-L20) The module note of that file describes the reduction: a hardness result that is valid over all finite fields leaves only a compression construction over prime fields to be supplied. [Realization.lean, lines 5–11](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Realization.lean#L5-L11) `Rounds.installable` states, for a finite field $F$, that a hypothesis on the algebraic closure of $F$ named `Prices.SharedPrice` implies `Rounds.Installable F`. It is in a file titled "Compression of tensor powers over finite fields". [Rounds/Installation.lean, lines 6–14](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Installation.lean#L6-L14)

## Limits of this note

The writer read this file and the statements it cites, and has not read the proofs behind `omega_eq_and_rigidity`. By the import lines, 511 of the 592 files in this module's import closure lie behind that theorem. The writer has not built the project. A reader who wants to know why the exponent is $9/4$ should start from `FieldFormula.lean` and follow both of its imports, `Realization.lean` and `Rounds/Installation.lean`.
