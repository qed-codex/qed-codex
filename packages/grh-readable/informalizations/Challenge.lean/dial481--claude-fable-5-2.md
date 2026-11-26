---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "license": "CC-BY-4.0"
}
---

# Informalization of Challenge.lean: the five statements about zeros of ζ and of Dirichlet L-functions

**This file states five theorems and proves none of them. The first two say that every zero of the Riemann zeta function other than $-2, -4, -6, \dots$ has real part $1/2$. The third says that no Dirichlet L-function has a zero with real part greater than $1/2$. The fourth says that every zero of a Dirichlet L-function in the strip $0 < \operatorname{Re} s < 1$ has real part $1/2$, and the fifth says the same for primitive characters only.** Each theorem ends in `sorry`. The file exists so that a checking tool can compare these statements with the ones in `src/Main.lean`, where the source gives its proofs.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file is 20 lines long. It imports one file, `src/Statements.lean`. [Line 1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L1) That file holds four definitions and imports only Mathlib. [Statements.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L1-L16) The comment at the top of this file says that nothing imports it. [Lines 3–5](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L3-L5)

The source's configuration for the tool Comparator names this file as the challenge and `Main` as the solution, lists the five theorem names, and permits the axioms `propext`, `Quot.sound` and `Classical.choice`. [Configuration](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/comparator.json) The source's README says that Comparator compares these statements with `src/Main.lean` and checks the proofs again. It reports that the authors ran Comparator on Linux, with a stand-in for its sandbox, and that it accepted the proofs. [README, section Checks](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#checks) The writer of this note has not built the project and has not run Comparator.

So this file answers one question: what exactly is claimed? Answering it takes this file, the four definitions in `src/Statements.lean`, and Mathlib's definitions of the zeta function, of Dirichlet characters and of their L-functions. The README's own advice to a reader who wants to trust the result is to read `src/Statements.lean`, the five statements in `src/Main.lean` and the list of axioms, and to build or replay the files. [README, section Theorems](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#theorems)

## The functions involved

**The zeta function.** `riemannZeta` is Mathlib's function $\zeta$. Mathlib defines it at every complex number, including the point $s = 1$ where the classical function has its pole. Statements 1 and 2 leave that point out by hypothesis.

**Dirichlet characters.** For an integer $N \ge 1$, a Dirichlet character modulo $N$ is a multiplicative character $\chi$ of the ring $\mathbb{Z}/N$ with complex values (`DirichletCharacter ℂ N`). The condition `[NeZero N]` in the statements says $N \ne 0$. The character written `1` is the trivial character modulo $N$, also called the principal character. A character is primitive when its conductor is $N$ itself, so that it does not come from a character of smaller modulus.

**L-functions.** `DirichletCharacter.LFunction χ` is Mathlib's $L(s, \chi)$: the meromorphic function on $\mathbb{C}$ that agrees with $\sum_{n \ge 1} \chi(n) n^{-s}$ wherever that series converges. [Mathlib, lines 52–60](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L52-L60) Modulo $1$ there is one character, and its L-function is $\zeta$. [Mathlib, lines 62–68](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L62-L68)

The Mathlib links point at revision `56a00585`, the one this project pins. [README, section Build](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#build)

## The five statements

**1. `riemannHypothesis`.** For every complex number $s$: if $\zeta(s) = 0$, and $s$ is not of the form $-2(n+1)$ for a natural number $n$, and $s \ne 1$, then

$$\operatorname{Re} s = \frac{1}{2}.$$

[Lines 7–8](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L7-L8) The type of this theorem is `RiemannHypothesis`, Mathlib's own formal statement of the Riemann Hypothesis. [Mathlib, lines 182–186](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L182-L186) The numbers $-2(n+1)$ are $-2, -4, -6, \dots$, the trivial zeros of $\zeta$.

**2. `riemannZeta_eq_zero_re`.** The same claim, written out in the project's own file as `RiemannZetaZerosOnLine`: the same three hypotheses and the same conclusion. [Lines 10–11](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L10-L11) [Statements.lean, lines 3–4](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L3-L4) Statements 1 and 2 are one claim under two names. The first name carries Mathlib's type, so a reader who trusts Mathlib's formulation does not have to read the project's.

**3. `LFunction_ne_zero_of_half_lt_re`.** For every $N \ge 1$, every Dirichlet character $\chi$ modulo $N$ and every complex number $s$ with $\operatorname{Re} s > 1/2$: if $\chi \ne 1$ or $s \ne 1$, then

$$L(s, \chi) \ne 0.$$

[Lines 13–14](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L13-L14) [Statements.lean, lines 6–8](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6-L8) The side condition removes one point for each modulus: $s = 1$ for the trivial character, where the L-function has its pole. For every other character the point $s = 1$ is included, and there the statement contains the classical fact $L(1, \chi) \ne 0$.

**4. `LFunction_eq_zero_re`.** For every $N \ge 1$, every Dirichlet character $\chi$ modulo $N$ and every complex number $s$ with $0 < \operatorname{Re} s < 1$: if $L(s, \chi) = 0$, then $\operatorname{Re} s = 1/2$. [Lines 16–17](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L16-L17) [Statements.lean, lines 10–12](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L10-L12) This is the Generalized Riemann Hypothesis for Dirichlet L-functions in its usual form, stated for all characters and not only for primitive ones.

**5. `LFunction_eq_zero_re_of_isPrimitive`.** Statement 4 with the extra hypothesis that $\chi$ is primitive. [Lines 19–20](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L19-L20) [Statements.lean, lines 14–16](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L14-L16)

## How the statements relate

Statement 5 is statement 4 for fewer characters, so 4 implies 5 at once.

Take $N = 1$ in statements 3 and 4. The only character is the trivial one and its L-function is $\zeta$. Statement 3 then says that $\zeta(s) \ne 0$ for $\operatorname{Re} s > 1/2$, $s \ne 1$. Statement 4 says that the zeros of $\zeta$ in the strip lie on the line. Statement 1 is slightly wider than that case of statement 4: it speaks of every zero of $\zeta$ apart from the listed exceptions, wherever it lies.

In the source, statement 3 is the one that the long argument is for. The others are derived from it: 1 and 4 by the symmetry $s \mapsto 1 - s$ of the zeros, 2 from 1, and 5 from 4. The note on `src/Main.lean` describes these steps.

## What the statements leave out

Statements 3, 4 and 5 say nothing about zeros with $\operatorname{Re} s \le 0$. The README states this as well. [README, section Theorems](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#theorems) In that region an L-function has its trivial zeros. An imprimitive character can have further zeros on the line $\operatorname{Re} s = 0$. Its L-function is that of the primitive character $\chi^{*}$ inducing it, multiplied by finitely many factors $1 - \chi^{*}(p)\, p^{-s}$. [Mathlib, lines 145–152](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L145-L152) Such a factor can vanish only where $\operatorname{Re} s = 0$, which the project proves as a lemma. [ZeroSymmetry.lean, lines 22–25](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L22-L25) The open strip $0 < \operatorname{Re} s < 1$ leaves those zeros out. That is why statement 4 can hold for all characters.

The statements say where zeros lie. They say nothing about how many there are or about their multiplicities. They concern $\zeta$ and Dirichlet L-functions only.

## What I read

I read `Challenge.lean`, `src/Statements.lean`, `comparator.json` and the README at the linked revision, and the Mathlib definitions cited above at the Mathlib revision that the project pins. All five theorem bodies in this file are `sorry`, by design. The section on how the statements relate also rests on my reading of `src/Main.lean` and `src/New/Main.lean`, described in the note on `src/Main.lean`. I did not build the project, run Comparator, or check that the proofs in `src/Main.lean` are accepted.
