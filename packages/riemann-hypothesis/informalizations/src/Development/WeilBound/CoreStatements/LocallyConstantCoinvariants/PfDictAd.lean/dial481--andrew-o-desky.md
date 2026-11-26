---
{
  "module": "src/Development/WeilBound/CoreStatements/LocallyConstantCoinvariants/PfDictAd.lean",
  "declarations": [
    "PositivityTheory.KCo.ad_act"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A scalar comparison of adelic and local operators

[Theorem REP.1334](https://andrewodesky.com/rh/lean/PositivityTheory.KCo.ad_act/)

Let $F$ be a number field, $I$ finite and $v$ a finite place of $F$. Fix a continuous additive character $\psi:\mathbb A_F\to\mathbb C^{\times}$ trivial on $F$ and equal to $x\mapsto\exp(-2\pi i\operatorname{Tr}_{F_\infty/\mathbb R}x)$ on adeles supported at infinity. Write $\mathcal S$ for finite linear combinations of products of archimedean Schwartz functions and finite-adelic locally constant compactly supported functions, and $\mathcal S_v=\mathcal S(F_v^I)$. A linear functional on all adelic functions is called admissible here if, after fixing any finite-adelic Schwartz factor, it is continuous in the archimedean Schwartz factor.

For $w=(\xi,\eta)$ define $[\rho_\psi(w)\Phi](x)=\psi(\eta\cdot x+\tfrac12\xi\cdot\eta)\Phi(x+\xi)$, and define the local action using $\psi_v(t)=\psi(1_vt)$. Let $T$ be a complex-linear endomorphism of all functions on $\mathbb A_F^I$, and let $L,L'$ be complex-linear endomorphisms of all functions on $F_v^I$. Let $s$ and $s_v$ be maps on the respective doubled coordinate spaces. Assume:

1. $T\mathcal S\subseteq\mathcal S$, and precomposition with $T$ preserves admissible functionals.
2. $T\rho_\psi(w)\Phi=\rho_\psi(sw)T\Phi$ for all $w$ and $\Phi\in\mathcal S$.
3. $L,L'$ preserve $\mathcal S_v$ and are inverse there.
4. $L\rho_{\psi_v}(w)\phi=\rho_{\psi_v}(s_vw)L\phi$ for $\phi\in\mathcal S_v$.
5. The $v$-component of $sw$ is $s_v(w_v)$ and $sw-w$ is supported at $v$.

There is $c\in\mathbb C$ such that, for every $\phi\in\mathcal S_v$ and every function $r$ invariant under translation by vectors supported at $v$ for which $x\mapsto\phi(x_v)r(x)$ belongs to $\mathcal S$, $$T\bigl(x\mapsto\phi(x_v)r(x)\bigr)=\bigl(x\mapsto c(L\phi)(x_v)r(x)\bigr).$$
