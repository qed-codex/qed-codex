---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Challenge.lean: the five statements about the permanent and the Hamiltonian cycle polynomial

**This file states five theorems and proves none. Three are lower bounds on the size of arithmetic circuits. The first says that there is a constant $c > 0$ such that over every field, for all $m$ above a threshold that depends only on the characteristic, every circuit for the $m \times m$ Hamiltonian cycle polynomial has more than $m^{c (\log_2 m)^{1/3}}$ gates, and so has every circuit for the permanent when the characteristic is not $2$. The second says the same for circuits that only approximate. The third is the case of the permanent over the real numbers. The other two are separations of classes: VP is a proper subset of VNP over every field, and VNP is not contained in the closure of VP.** All five end in `sorry`. The definitions are in a second file, `Statement.lean`, which this note reads as well.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 33 lines. It imports `Statement.lean` and nothing else. [Line 6](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L6) Its header says that it holds the theorems of `Solution.lean` with `sorry` in place of their proofs, for the tool Comparator, that `Statement.lean` imports Mathlib alone, and that nothing imports this file. [Lines 8–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L8-L9) `Statement.lean` imports only Mathlib and describes itself as definitions and statements. [Statement.lean, lines 6–12](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L6-L12)

The five theorems are `mainTheorem`, `mainTheoremApprox`, `separation`, `separationClosure` and `permanent_over_real`, in the namespace `Solution`. Each has the body `sorry`. [Lines 11–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L11-L31) The project's Comparator configuration names this file as the challenge module and `Solution` as the solution module. It lists the five theorem names and permits the axioms `propext`, `Quot.sound` and `Classical.choice`. [comparator.json, lines 1–18](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/comparator.json#L1-L18) The README says that Comparator compares the statements with this file and checks the proofs again with a second kernel. [README, line 25](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L25) I have not built the project and have not run Comparator.

## Circuits and their size

`Computes f s` says that the polynomial $f$ has an arithmetic circuit with at most $s$ gates. In detail: there is a list of $s$ polynomials that contains $f$, and each entry is a variable, a constant, or the sum or the product of two earlier entries, which may be the same entry twice. Variables and constants count as gates. [Statement.lean, lines 20–27](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L20-L27) The only operations are addition and multiplication.

## The two polynomials

Both are polynomials in the $m^2$ variables $X_{i,j}$ with $0 \le i, j < m$.

- The permanent is $\operatorname{perm}_m = \sum_{\sigma} \prod_i X_{\sigma(i), i}$, the sum over all permutations $\sigma$ of $\{0, \dots, m-1\}$. [Statement.lean, lines 29–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L29-L31)
- The Hamiltonian cycle polynomial is $\operatorname{hc}_m = \sum_{\sigma} \prod_i X_{i, \sigma(i)}$, the sum over those permutations that are one cycle through all $m$ points. [Statement.lean, lines 33–36](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L33-L36)

## The bound

`Beyond c m s` is the inequality $m^{c (\log_2 m)^{1/3}} < s$. [Statement.lean, lines 38–39](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L38-L39) For $m \ge 1$ the left side equals $2^{c (\log_2 m)^{4/3}}$. This is a quasi-polynomial bound. For $c > 0$ it grows faster than every fixed power of $m$ and more slowly than $2^{m^{\epsilon}}$ for every $\epsilon > 0$.

## Statements 1 and 2: the lower bounds

`MainTheorem` says: there is a real number $c > 0$ such that for every natural number $p$ there is an $m_0$ with the following property. For every field $F$ of characteristic $p$, every $m \ge m_0$ and every $s$: if $\operatorname{hc}_m$ over $F$ has a circuit with at most $s$ gates, then $s > m^{c (\log_2 m)^{1/3}}$. If $p \ne 2$, the same holds for $\operatorname{perm}_m$. [Statement.lean, lines 41–46](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L41-L46)

The order of the quantifiers matters. The constant $c$ does not depend on the field or on its characteristic. The threshold $m_0$ may depend on the characteristic $p$, and on nothing else about the field. If $p$ is neither $0$ nor a prime, no field has characteristic $p$, and the statement says nothing for that $p$.

`MainTheoremApprox` has the same form with `Approximates` in place of `Computes`. [Statement.lean, lines 57–60](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L57-L60) `Approximates f s` speaks of circuits over the field of Laurent series in a new variable $\varepsilon$ over $F$. Every such series may be used as a constant. The definition says that some polynomial $q$ over that field has a circuit with at most $s$ gates and that $q = f + \varepsilon g$, where the coefficients of $g$ are power series in $\varepsilon$. In the Lean text this reads: in every coefficient of $q$, the coefficient of $\varepsilon^i$ is $0$ for $i < 0$, and for $i = 0$ it is the matching coefficient of $f$. [Statement.lean, lines 50–55](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L50-L55)

## Statements 3 and 4: the classes

A family consists of, for every $n$, a finite set of variables and a polynomial in them. [Statement.lean, lines 64–71](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L64-L71)

- **VP.** A family is in VP if there is a number $a$ such that, for every $n$, the number of variables, the total degree and the size of some circuit of the $n$-th polynomial are all at most $n^a + a$. [Statement.lean, lines 75–78](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L75-L78)
- **The closure of VP.** The same, with approximating circuits. [Statement.lean, lines 80–83](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L80-L83)
- **VNP.** A family $f$ is in VNP if there are numbers $r(n)$ and a family $g$ in VP with the following property. The polynomial $g_n$ has the variables of $f_n$ and $r(n)$ further variables, and $f_n(x) = \sum_e g_n(x, e)$, the sum over all vectors $e$ of $r(n)$ bits. [Statement.lean, lines 85–90](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L85-L90)

`Separation` says that over every field VP is a proper subset of VNP. `SeparationClosure` says that over every field VNP is not contained in the closure of VP. [Statement.lean, lines 92–96](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L92-L96)

## Statement 5: the permanent over the real numbers

The last theorem is written out without a named proposition: there are $c > 0$ and $m_0$ such that for all $m \ge m_0$ every circuit for $\operatorname{perm}_m$ over $\mathbb{R}$ has more than $m^{c (\log_2 m)^{1/3}}$ gates. [Lines 29–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L29-L31) It is the case $p = 0$, $F = \mathbb{R}$ of the second half of statement 1.

## How the statements relate

The file states the five separately and says nothing about how they depend on each other. The project README presents the two separations as consequences of the two lower bounds. [README, line 3](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L3) The first four statements carry a universe parameter. So there is one statement for each universe of types, about the fields in it, and $c$ and $m_0$ are chosen for each universe. [Lines 15–27](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L15-L27)

## What the statements leave out

- **Proofs.** This file has none.
- **The constants.** The statements say that $c$ and $m_0$ exist. They give no values.
- **The permanent in characteristic 2.** No bound is claimed there. (Background that is not in the source: in characteristic $2$ the permanent equals the determinant.)
- **P and NP.** The README says that this does not settle P vs NP. [README, line 3](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L3)
- **Review by people.** The README says that the paper and the formalization were written by AI models and that no human mathematician has checked the proof. [README, line 5](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L5) It also says that Lean checks the proofs, but that no machine checks that `Statement.lean` says what is claimed. [README, line 15](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L15)

## What I read

I read this file and `Statement.lean` in full, and the Comparator configuration and the README, at the linked revision. I did not read the paper. I did not read the proofs, and I did not build the project.
