---
{
  "module": "src/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "license": "CC-BY-4.0"
}
---

# Informalization of Main.lean: how the five theorems are obtained from one

**This file derives the five theorems from one, in 22 lines. That one says that no Dirichlet L-function vanishes where $\operatorname{Re} s > 1/2$. The file takes it directly from a theorem called `New.grh`, which lives in another file. Two of the other four follow from it by the symmetry $s \mapsto 1 - s$ of the zeros. The remaining two are a restatement and a special case of those. All of the difficulty is inside `New.grh`, which this file imports and does not prove.** Whether Lean accepts the whole is reported by the source's README and was not checked for this note.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What this note covers

The file is short, so this note also goes further down: the two lemmas that carry out the symmetry argument, the last step in the proof of `New.grh`, and the statements from which the same file assembles the bound that this step needs. It stops there. The section at the end says what was read and what was not.

The statements themselves are explained in the note on `Challenge.lean`. They are numbered here in the order of the file.

## The file itself

The first line is a comment: the proof is Levent Alpöge's, with Claude. [Line 1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L1) The file imports one module, `New.Main`. [Line 2](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L2) Then come the five theorems.

1. `riemannHypothesis` applies the lemma `New.zeta_zeros_on_line` to `New.grh`. [Lines 4–5](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L5) The lemma's conclusion has the project's type `RiemannZetaZerosOnLine`, and the theorem is declared with Mathlib's type `RiemannHypothesis`. Lean accepts this only if the two unfold to the same proposition.
2. `riemannZeta_eq_zero_re` cites theorem 1 with no further argument. [Lines 7–8](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L7-L8) Its type is the project's `RiemannZetaZerosOnLine`, so this is the same identification in the other direction.
3. `LFunction_ne_zero_of_half_lt_re` is `New.grh` itself. [Lines 10–13](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L10-L13)
4. `LFunction_eq_zero_re` applies the lemma `New.zeros_on_line` to `New.grh`. [Lines 15–17](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L15-L17)
5. `LFunction_eq_zero_re_of_isPrimitive` applies theorem 4 and does not use the hypothesis that the character is primitive. [Lines 19–22](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L19-L22)

So the file has three inputs: the theorem `New.grh` and the two lemmas.

## From the half-plane to the critical line

Both lemmas are in `src/New/Main.lean`. Each takes the half-plane statement as a hypothesis, called $h$ below: for every Dirichlet character $\chi$ and every $s$ with $\operatorname{Re} s > 1/2$, if $\chi \ne 1$ or $s \ne 1$ then $L(s, \chi) \ne 0$. [New/Main.lean, lines 21–23](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L21-L23)

**Dirichlet L-functions: `New.zeros_on_line`.** Let $L(s, \chi) = 0$ with $0 < \operatorname{Re} s < 1$. [New/Main.lean, lines 25–42](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L25-L42)

- Neither $s$ nor $1 - s$ equals $1$.
- A separate lemma gives the symmetry of the zeros: if $L(s, \chi) = 0$, $\operatorname{Re} s \ne 0$ and $s \ne 1$, then either $s$ is a pole of the gamma factor of $\chi$, or $L(1 - s, \chi^{-1}) = 0$. [ZeroSymmetry.lean, lines 55–63](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L55-L63)
- The gamma factor has no pole where $\operatorname{Re} s > 0$. So $L(1 - s, \chi^{-1}) = 0$.
- Now $h$ applies to both zeros. A zero of $L(\cdot, \chi)$ at $s$ with $\operatorname{Re} s > 1/2$ would contradict $h$, so $\operatorname{Re} s \le 1/2$. In the same way $\operatorname{Re}(1 - s) \le 1/2$. Together, $\operatorname{Re} s = 1/2$.

One convention is in play. Mathlib gives the gamma factor the value $0$ at its poles, so "is a pole" is written in the source as "equals $0$". The source comments say this. [New/Main.lean, lines 32–33](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L32-L33)

The symmetry lemma holds for every character, primitive or not. Its proof passes to the primitive character $\psi$ that induces $\chi$. The L-functions of $\chi$ and $\psi$ differ by finitely many Euler factors, and these do not vanish where $\operatorname{Re} s \ne 0$, so $L(s, \psi) = 0$ as well. [ZeroSymmetry.lean, lines 22–25](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L22-L25) If $s$ is not a pole of the gamma factor, Mathlib's functional equation, applied to $\psi^{-1}$, gives $L(1 - s, \psi^{-1}) = 0$, and then $L(1 - s, \chi^{-1}) = 0$. [ZeroSymmetry.lean, lines 64–82](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L64-L82) The file classes this as a known result and names Montgomery and Vaughan, Multiplicative Number Theory I, Corollaries 10.3 and 10.8, as its source. [ZeroSymmetry.lean, lines 10–14](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L10-L14) I have not compared the lemma with that book.

**The zeta function: `New.zeta_zeros_on_line`.** Let $\zeta(s) = 0$, where $s \ne 1$ and $s$ is none of $-2, -4, -6, \dots$ [New/Main.lean, lines 44–65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L44-L65)

- $s \ne 0$, because $\zeta(0) = -1/2$.
- The factor $\Gamma_{\mathbb{R}}$ has its poles at $0, -2, -4, \dots$, and $s$ is none of these.
- So the completed zeta function vanishes at $s$. It is symmetric under $s \mapsto 1 - s$, so it vanishes at $1 - s$, and therefore $\zeta(1 - s) = 0$.
- $\zeta$ is the L-function of the character modulo $1$. Neither $s$ nor $1 - s$ equals $1$, so $h$ applies to both and gives $\operatorname{Re} s \le 1/2$ and $1 - \operatorname{Re} s \le 1/2$. Together, $\operatorname{Re} s = 1/2$.

This argument does not ask where the zero lies. It covers every zero of $\zeta$ that meets the hypotheses of statement 1.

## The theorem everything rests on

`New.grh` is the last theorem of `src/New/Reduction/OneSidedBound.lean`. Its statement is statement 3. [OneSidedBound.lean, lines 237–267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L237-L267) Write $\rho$ for the point and $q$ for the modulus of $\chi$. The proof in that file runs as follows.

**The point 1.** If $\rho = 1$ then $\chi$ is not trivial, and $L(1, \chi) \ne 0$ is in Mathlib. [OneSidedBound.lean, lines 243–245](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L243-L245) [Mathlib, lines 395–400](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/Nonvanishing.lean#L395-L400)

**A remainder term.** Otherwise choose $\beta$ with $1/2 < \beta < \operatorname{Re} \rho$, and put $q_0 = 18480\,q$ and $d_0 = 9240\,q - 1$. For a prime $d$, let $\lambda(n) = \Lambda(n)\,\bigl(1 - (n/d)\bigr)$ when $n \equiv 1 \pmod{q_0}$ and $\lambda(n) = 0$ otherwise, where $\Lambda$ is the von Mangoldt function and $(n/d)$ the Legendre symbol. [PrimeError.lean, lines 43–45](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L43-L45) The remainder is

$$R(x) = \sum_{n \le x} \lambda(n) \left( \frac{1}{n} - \frac{1}{x} \right) - \frac{\log x}{\varphi(q_0)} - c,$$

with a constant $c$ that depends on $d$ and $q_0$. [PrimeError.lean, lines 60–66](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L60-L66)

**The criterion.** A theorem called the one-sided criterion says: let $q_0$ be a positive multiple of $8$, let $d_0 \equiv 7 \pmod 8$ be prime to $q_0$, and let $\beta > 1/2$. Suppose that for each prime $d \equiv d_0 \pmod{q_0}$ we have $R(x) \le x^{\beta - 1}$ for all large $x$. Then $L(\rho, \psi) \ne 0$ for every character $\psi$ modulo $q_0$ and every $\rho \ne 1$ with $\operatorname{Re} \rho > \beta$. [Criterion.lean, lines 31–42](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L31-L42) Only an upper bound on $R$ is assumed, not a bound on $|R|$. That is the sense of "one-sided".

**The bound.** A theorem called the one-sided bound supplies the hypothesis: for $q_0$ a positive multiple of $18480$, a prime $d \equiv q_0/2 - 1 \pmod{q_0}$ and every $\varepsilon > 0$, we have $R(y) \le y^{-1/2 + \varepsilon}$ for all large real $y$. [OneSidedBound.lean, lines 197–202](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L197-L202) With $\varepsilon = \beta - 1/2$ this is the bound $x^{\beta - 1}$ that the criterion asks for. The numbers $q_0$ and $d_0$ above are chosen so that both theorems apply: $d_0 = q_0/2 - 1$. [OneSidedBound.lean, lines 246–262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L246-L262)

**Back to $\chi$.** The criterion now gives a nonzero value at $\rho$ for the character modulo $q_0$ induced by $\chi$. Its L-function is $L(s, \chi)$ times finitely many factors, by a Mathlib lemma. A product that is not zero has no zero factor, so $L(\rho, \chi) \ne 0$. [OneSidedBound.lean, lines 263–267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L263-L267) [Mathlib, lines 145–152](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L145-L152)

## Where the one-sided bound comes from

The same file assembles the one-sided bound from three statements. Each is given here as that file states it. Their own proofs draw on other files, which I did not read. Fix $\delta$ with $0 < \delta < 1/100$.

- From the main inequality the file derives a bound for a bundle of choices that the source calls admissible data. Among the data are an integer $x$, two much larger scales $x_1$ and $b$, and an integer $m$ between $\sqrt{x}$ and $2\sqrt{x}$. The bound is $R_{q_0}(x) \le \varphi(q_0) \log^6 b / m + |R_{q_0}(x_1)| + \log b \cdot |R_1(x_1)|$, where the subscript is the modulus. [OneSidedBound.lean, lines 27–35](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L27-L35) The main inequality itself is `star_inequality`. [MainInequality.lean, lines 82–88](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L82-L88)
- Such data exist for every large integer $x$, with $\log b \le 2x^{\delta}$ and $\log x_1 \ge x^{\delta/12}$. [OneSidedBound.lean, lines 69–76](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L69-L76)
- By the prime number theorem, for every large integer $x$ both remainders are at most $x^{-2}$ in absolute value at every point $e^{l}$ with $l \ge x^{\delta/12}$, and so at $x_1$. [OneSidedBound.lean, lines 91–98](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L91-L98)

Put together, $R(x) \le (64\,\varphi(q_0) + 3)\, x^{-1/2 + 6\delta}$ for all large integers $x$. [OneSidedBound.lean, lines 119–128](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L119-L128) The theorem applies this with a $\delta$ such that $7\delta \le \varepsilon$, passes from integers to real numbers, and lets one factor $y^{\delta}$ absorb the constant. [OneSidedBound.lean, lines 197–235](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L197-L235)

## What I read and what I did not

I read `src/Main.lean`, `src/New/Main.lean` and `src/New/Reduction/OneSidedBound.lean` in full, the symmetry lemma with its proof, the statements of the one-sided criterion and of the main inequality, and the definition of the remainder. I read the Mathlib statements cited above at the Mathlib revision that the project pins.

I did not read the proof of the criterion, the proof of the main inequality, the existence of the data, the prime number theorem input, or anything those depend on. That is nearly all of the project: the README counts about 300,000 lines of code, in 495 files under `src/Lib` and 306 under `src/New`. [README, section Layout](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#layout) I did not build the project.

This note describes how the top of the proof is put together. It is not evidence that the proof is correct. The README reports that every file compiles without `sorry`, that the five theorems depend only on the axioms `propext`, `Classical.choice` and `Quot.sound`, and that independent checkers accept an export of them. [README, section Checks](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#checks)
