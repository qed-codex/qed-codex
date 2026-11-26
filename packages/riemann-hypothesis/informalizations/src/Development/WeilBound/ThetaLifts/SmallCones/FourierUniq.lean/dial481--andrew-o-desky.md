---
{
  "module": "src/Development/WeilBound/ThetaLifts/SmallCones/FourierUniq.lean",
  "declarations": [
    "PositivityTheory.ThKCT.thetaInj_of",
    "PositivityTheory.ThKCT.thetaUniq_of"
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

## Uniqueness of the rationally invariant theta functional

[Theorem REP.1362](https://andrewodesky.com/rh/lean/PositivityTheory.ThKCT.thetaUniq_of/)

Let $F$ be a number field, $I$ a finite set, and $\psi:\mathbb A_F\to\mathbb C^\times$ a continuous additive character trivial on $F$, whose restriction to adeles supported at infinity is $x\mapsto\exp(-2\pi i\operatorname{Tr}_{F_\infty/\mathbb R}x)$. Let $\lambda$ be a complex-linear functional on functions on $\mathbb A_F^I$ such that, after fixing any finite-adelic locally constant compactly supported factor, its value on the product is continuous in the archimedean Schwartz factor, and let $\mathcal S(\mathbb A_F^I)$ denote the adelic Schwartz space defined below. For $\xi,\eta\in F^I$ define $$[\rho_\psi(\xi,\eta)\Phi](x)=\psi\!\left(\eta\cdot x+\tfrac12\xi\cdot\eta\right)\Phi(x+\xi).$$ If $$\lambda(\rho_\psi(\xi,\eta)\Phi)=\lambda(\Phi)\qquad(\xi,\eta\in F^I,\ \Phi\in\mathcal S(\mathbb A_F^I)),$$ then there is $c\in\mathbb C$ such that $$\lambda(\Phi)=c\sum_{x\in F^I}\Phi(x)\qquad(\Phi\in\mathcal S(\mathbb A_F^I)).$$

## Schrodinger translates of theta summation detect a function

[Theorem THETA.1449](https://andrewodesky.com/rh/lean/PositivityTheory.ThKCT.thetaInj_of/)

Let $F$ be a number field, $I$ a finite set, and $\psi:\mathbb A_F\to\mathbb C$ a standard continuous additive character, trivial on $F$. The standard-character condition also fixes $\psi(a)=\exp(-2\pi i\operatorname{Tr}_{F_\infty/\mathbb R}(a_\infty))$ on adeles with zero finite component, where $F_\infty=F\otimes_{\mathbb Q}\mathbb R$. On the adelic Schwartz space $\mathcal S(\mathbb A_F^I)$ define the Schrodinger action by $\bigl(\rho_\psi(a,b)\Phi\bigr)(x)=\psi(\sum_i x_i b_i+\tfrac12\sum_i a_i b_i)\Phi(x+a)$ for $a,b\in\mathbb A_F^I$, and put $$\Theta(\Phi)=\sum_{x\in F^I}\Phi(x).$$ If $\Phi\in\mathcal S(\mathbb A_F^I)$ satisfies $$\Theta(\rho_\psi(w)\Phi)=0\qquad\text{for every translation-modulation parameter }w,$$ then $\Phi=0$.
