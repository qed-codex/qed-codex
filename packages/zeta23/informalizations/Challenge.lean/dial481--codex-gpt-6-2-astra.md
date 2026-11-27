---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Counting distinct and simple zeros in height windows

AI drafted this autoinformalization from the original source. It is open for mathematical review.

Consider the zeros of the Riemann zeta function in the open strip $0<\operatorname{Re}\rho<1$ with $T<\operatorname{Im}\rho\le2T$. The challenge counts them in several ways. A zero of order three contributes three to `Ncount`, one to `Ndist`, and nothing to `N0simple`. If it lies on the critical line it also contributes one to `N0star`. These choices determine what each proportion means. [Challenge.lean lines 50–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L50-L80)

The first six targets use either the window $(T,2T]$ or the cumulative window $(0,T]$. They give lower proportions of $2/3$ for distinct zeros on the line, $2/3$ for simple zeros on the line, and $5/6$ for all distinct zeros. Formally each bound allows any positive error $ε$ and holds for every sufficiently large $T$, with the threshold allowed to depend on $ε$. Multiplying the total count by the proposed proportion minus $ε$ avoids dividing by a count that might be zero. [Challenge.lean lines 127–159](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L127-L159)

The later targets use a constant `cMT` defined by a trigonometric expression. The on-line proportion becomes $2-1/\mathrm{cMT}$ and the distinct proportion becomes $(3-1/\mathrm{cMT})/2$. The challenge also asks for dyadic-window estimates for the L-function of each primitive Dirichlet character of modulus greater than one. [Challenge.lean lines 112–120](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L112-L120) · [Challenge.lean lines 161–186](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L161-L186) · [Challenge.lean lines 188–229](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L188-L229)

I read the challenge’s definitions and its seventeen theorem statements. They use `sorry` on the statement side. I did not build the project or audit the analytic estimates. [Challenge.lean lines 6–29](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L6-L29)
