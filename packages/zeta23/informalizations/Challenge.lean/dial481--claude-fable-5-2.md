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

# Informalization of Challenge.lean: seventeen statements on the proportion of zeros on the critical line

**This file states seventeen theorems and proves none. Each is a lower bound on a proportion of zeros, in this form: for every $\varepsilon > 0$ and all large $T$, at least $c - \varepsilon$ of the nontrivial zeros in a window of height $T$ have a certain property. For the Riemann zeta function the theorems say this with $c = 2/3$ for the zeros on the critical line, with $c = 2/3$ for the zeros that are simple and on the line, and with $c = 5/6$ for distinct zeros. They give bounds of the same three kinds with the larger constants $2 - 1/c_1^*$ and $(3 - 1/c_1^*)/2$, for a constant $c_1^*$ in closed form. By the source's decimals these are $0.67250\ldots$ and $0.83625\ldots$. Six further theorems give all of these bounds for the zeros of $L(s, \chi)$, for every primitive Dirichlet character $\chi$ modulo $q > 1$. The header says that the statements are forms of the headline assertions of a paper by Levent Alpöge and Ralph Furman.** Each theorem ends in `sorry`. The file carries its own definitions and imports only Mathlib.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 231 lines. Its only import is Mathlib. [Line 29](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L29) The header calls it the trusted challenge module. It says that the file holds seventeen statements about the zeros of Mathlib's `riemannZeta` and of Mathlib's `DirichletCharacter.LFunction`, each with the proof `sorry`, and that these are forms of the headline assertions of Theorems A to E of the paper, each at the constant stated in the paper. [Lines 7–11](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L7-L11) The project README gives the paper: "More than two thirds of the zeta zeros are simple and on the critical line" by Levent Alpöge and Ralph Furman, arXiv:2608.13637. [README, line 12](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/README.md?plain=1#L12)

The labels A to E are the repository's own. The README says that in the arXiv version of the paper B and C are Theorem A (i) and (ii), D is the improvement stated with them, E is Theorem B, and A is a companion statement recorded in the paper's Appendix A. [README, lines 68–71](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/README.md?plain=1#L68-L71) This note uses the repository's labels.

The definitions that the statements need are copied into this file from a module `ChallengeDeps.lean`, so that nothing but Mathlib is imported. [Lines 31–41](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L31-L41) The header says that `Solution.lean` proves exactly these statements and that the tool Comparator checks that the statements are equal and that only the axioms `propext`, `Classical.choice` and `Quot.sound` are used. [Lines 22–24](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L22-L24) The Comparator configuration lists the seventeen names. [comparator.json, lines 4–22](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/comparator.json#L4-L22) I have not built the project and have not run Comparator.

## The counting functions

All counts are over a window of ordinates $T_1 < \operatorname{Im} \rho \le T_2$.

- A nontrivial zero is a $\rho$ with $\zeta(\rho) = 0$ and $0 < \operatorname{Re} \rho < 1$. [Lines 50–54](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L50-L54)
- The multiplicity of $\rho$ is the order of vanishing of $\zeta$ at $\rho$. [Lines 56–59](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L56-L59)
- $N(T_1, T_2)$ is the number of nontrivial zeros in the window, counted with multiplicity. The source notes that the window holds finitely many zeros, and that this is proved on the solution side and not assumed. [Lines 61–68](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L61-L68)
- $N_d(T_1, T_2)$ counts each distinct zero in the window once. [Lines 70–72](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L70-L72)
- $N_0^*(T_1, T_2)$ counts the distinct zeros in the window with $\operatorname{Re} \rho = 1/2$. [Lines 74–76](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L74-L76)
- $N_0^s(T_1, T_2)$ counts those zeros on the line that have multiplicity exactly $1$. [Lines 78–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L78-L80)

The same definitions are made for $L(s, \chi)$, where $\chi$ is a Dirichlet character modulo $q \ne 0$ and $L(s, \chi)$ is Mathlib's analytic continuation. [Lines 82–110](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L82-L110)

The constant of Theorem D is $c_1^* = \sqrt{2} \tan\vartheta / (1 + \vartheta \tan\vartheta)$ at $\vartheta = 1/\sqrt{2}$. The source gives $c_1^* = 0.7532960\ldots$, $2 - 1/c_1^* = 0.67250\ldots$ and $(3 - 1/c_1^*)/2 = 0.83625\ldots$, and adds that the decimals are not part of the formal statements. [Lines 114–120](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L114-L120)

## The form of every statement

A bound "$\liminf X(T)/N(T) \ge c$" is written without a limit: for every $\varepsilon > 0$ there is a $T_0$ such that $(c - \varepsilon) N(T) \le X(T)$ for all $T \ge T_0$. [Lines 14–15](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L14-L15) There are two kinds of window. The dyadic window is $(T, 2T]$. The cumulative window is $(0, T]$. [Line 16](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L16)

## The seventeen statements

For the zeta function there are eleven.

- **Theorem A.** $(2/3 - \varepsilon) N \le N_0^*$, on dyadic and on cumulative windows. [Lines 127–138](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L127-L138)
- **Theorem B.** $(2/3 - \varepsilon) N \le N_0^s$, on both kinds of window. [Lines 140–149](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L140-L149)
- **Theorem C.** $(5/6 - \varepsilon) N \le N_d$, on both kinds of window. [Lines 151–159](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L151-L159)
- **Theorem D.** With $c_1^*$ as above: $(2 - 1/c_1^* - \varepsilon) N \le N_0^*$ on dyadic windows; the same bound for $N_0^s$ on both kinds of window; and $(3/2 - 1/(2 c_1^*) - \varepsilon) N \le N_d$ on both kinds of window. [Lines 161–186](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L161-L186)

For $L(s, \chi)$ there are six. Each assumes that $\chi$ is primitive and that $q > 1$, and each is on dyadic windows.

- **Theorem E.** The bounds of Theorems A, B and C. [Lines 188–208](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L188-L208)
- **Theorem E, with the constants of Theorem D.** The three bounds of Theorem D. [Lines 210–229](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L210-L229)

## Points that need care

- **What "two thirds of the zeros" means.** On the left side the zeros are counted with multiplicity. On the right side they are counted as distinct points. The source says so in the comment on Theorem A. [Lines 127–130](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L127-L130)
- **Nontrivial means in the open strip.** The source remarks that every zero in the strip is nontrivial in the usual sense, and that the converse is classical and is not needed to state the theorems. [Lines 50–53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L50-L53)
- **Only positive ordinates.** A window is $T_1 < \operatorname{Im} \rho \le T_2$, not a bound on $|\operatorname{Im} \rho|$. [Lines 61–63](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L61-L63) The definition takes any real $T_1$ and $T_2$. The theorems use only the windows $(T, 2T]$ and $(0, T]$ for large $T$, so they count zeros with positive ordinate. [Lines 127–229](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L127-L229)
- **The counts rest on finiteness.** The four counts are written with Mathlib's finite sum and with the number of elements of a set. In Mathlib both give $0$ for an infinite set. So the statements mean what they say only because a window holds finitely many zeros, which the source says is proved on the solution side. The multiplicity is likewise $0$ where the order of vanishing is infinite. [Lines 56–68](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L56-L68)
- **Dependence of $T_0$.** In each statement $T_0$ may depend on $\varepsilon$, and in Theorem E also on $\chi$. No value is given.

## What the statements leave out

- **Proofs.** This file has none.
- **All zeros.** The statements bound proportions from below. They do not say that every zero is on the line.
- **A second topic.** The repository has a separate set of six statements about the zeros of $\xi'$, with its own challenge file. This note does not cover it. [README, lines 39–41](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/README.md?plain=1#L39-L41)
- **Who wrote and who checked.** The project's metadata says that all Lean code was written by Claude and that the trusted statement file was read against the paper by a paper author. [formalization.yaml, lines 27–28](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/formalization.yaml#L27-L28)

## What I read

I read this file in full, the Comparator configuration, lines 1 to 41 and 60 to 71 of the README and the description in `formalization.yaml`, at the linked revision. I did not compare the definitions with `ChallengeDeps.lean`. I did not read the paper. I did not read the proofs, and I did not build the project.
