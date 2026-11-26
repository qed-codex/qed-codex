---
{
  "module": "src/Development/WeilBound/CoreStatements/LocallyConstantCoinvariants/PfDictMod.lean",
  "declarations": [
    "PositivityTheory.KCo.cyclicity",
    "PositivityTheory.KCo.model_existence"
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

## Symplectic covariance on nonarchimedean Schwartz spaces

[Theorem REP.1346](https://andrewodesky.com/rh/lean/PositivityTheory.KCo.model_existence/)

Let $k$ be a nonarchimedean local field in which $2$ is invertible, let $I,J$ be finite sets, and let $\psi:k\to\mathbb C^\times$ be a continuous nontrivial additive character. On $k^I\oplus k^I$ use the alternating form $$\langle(\xi,\eta),(\xi',\eta')\rangle=\xi\cdot\eta'-\xi'\cdot\eta.$$ Let $e:k^J\oplus k^J\to k^I\oplus k^I$ be a linear isomorphism preserving these alternating forms. Write $$[\rho_\psi(\xi,\eta)f](x)=\psi\!\left(\eta\cdot x+\tfrac12\xi\cdot\eta\right)f(x+\xi).$$ There is a complex-linear map $U:\mathbb C^{k^I}\to\mathbb C^{k^J}$ whose restriction is a bijection $\mathcal S(k^I)\to\mathcal S(k^J)$ and satisfies $$U\rho_\psi(e w)f=\rho_\psi(w)Uf\qquad(w\in k^J\oplus k^J,\ f\in\mathcal S(k^I)).$$ Here $\mathcal S$ is the space of locally constant compactly supported functions.

## Cyclicity of every nonzero local Schwartz function

[Theorem REP.1634](https://andrewodesky.com/rh/lean/PositivityTheory.KCo.cyclicity/)

Let $k$ be a nonarchimedean local field in which $2$ is invertible, $I$ a finite set, and $\psi:k\to\mathbb C$ a continuous nontrivial additive character. For $a,b\in k^I$ define $$(R_\psi(a,b)\phi)(x)=\psi\!\left(\sum_i x_i b_i+\tfrac12\sum_i a_i b_i\right)\phi(x+a).$$ Let $\mathcal S(k^I)$ denote the locally constant compactly supported complex functions. If $0\ne\phi_0\in\mathcal S(k^I)$ and $L:(k^I\to\mathbb C)\to\mathbb C$ is complex linear with $$L(R_\psi(a,b)\phi_0)=0\qquad(a,b\in k^I),$$ then $L(\phi)=0$ for every $\phi\in\mathcal S(k^I)$. No continuity is required of $L$.
