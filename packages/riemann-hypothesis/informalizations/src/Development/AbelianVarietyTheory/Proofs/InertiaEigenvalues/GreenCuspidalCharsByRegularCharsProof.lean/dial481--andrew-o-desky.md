---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GreenCuspidalCharsByRegularCharsProof.lean",
  "declarations": [
    "GlobalTheory.greenRegularCharacters_holds"
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

## Cuspidal characters of finite general linear groups

[Theorem REP.0109](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)

Let $p$ be prime, $d\ge1$, and $K=\mathbb F_{p^d}$. A character $\theta:K^\times\to\mathbb C^\times$ is regular if its $d$ Frobenius conjugates are distinct. There are cuspidal characters $\chi_\theta$ of $\mathrm{GL}_d(\mathbb F_p)$ for regular $\theta$, with $$\chi_\theta(1)=\prod_{i=1}^{d-1}(p^i-1).$$ If $g\in\mathrm{GL}_d(\mathbb F_p)$ has irreducible characteristic polynomial and $z\in K^\times$ is a root, then $$\chi_\theta(g)=(-1)^{d-1}\sum_{i=0}^{d-1}\theta(z^{p^i}).$$ Here $\theta^{p^i}(z)=\theta(z^{p^i})$. Two regular parameters give the same character exactly when $\theta'=\theta^{p^i}$ for some $0\le i<d$; every cuspidal character arises in this way.

For a polynomial parametrization, choose such a family $\theta\mapsto\chi_\theta$. Fix an algebraic closure $\overline{\mathbb F}_p$ and identify $K$ with its subfield of $p^d$ elements. Choose an injective multiplicative map $\tau:\overline{\mathbb F}_p^{\times}\to\mathbb C^{\times}$ and generators $\gamma_e\in\mathbb F_{p^e}^{\times}$ for every $e\ge1$, satisfying $$\gamma_{er}^{(p^{er}-1)/(p^e-1)}=\gamma_e\qquad(e,r\ge1).$$ For every monic irreducible $P\in\mathbb F_p[T]$ of degree $d$ with $P(0)\ne0$, choose a root $x\in K^{\times}$ and define the regular character $$\theta_x(\gamma_d^n)=\tau(x)^n\qquad(n\in\mathbb Z).$$ Then $\chi_P=\chi_{\theta_x}$ is independent of the chosen root, and $P\mapsto\chi_P$ is a bijection onto the cuspidal characters of $\mathrm{GL}_d(\mathbb F_p)$. Each $\chi_P$ has the degree and values given by the formulas above with $\theta=\theta_x$. **Squarefree polynomial form.** For every prime $p$ and integer $N\ge1$, let $\mathscr S_{p,N}$ be the set of monic squarefree polynomials $f\in\mathbb F_p[T]$ of degree $N$ with $f(0)\ne0$. There are nonzero irreducible finite-dimensional complex representations $\rho_f$ of $\mathrm{GL}_N(\mathbb F_p)$ on spaces $V_f$, indexed by $f\in\mathscr S_{p,N}$, whose characters $\chi_f$ are pairwise distinct. If the distinct monic irreducible factors of $f$ have degrees $d_1,\ldots,d_t$, then $$\chi_f(1)\prod_{j=1}^t(p^{d_j}-1)=\prod_{i=1}^N(p^i-1).$$ For every $f\in\mathscr S_{p,N}$ there are a nontrivial additive character $\psi_f:\mathbb F_p\to\mathbb C^\times$, coefficients $c_{f,a}\in\mathbb F_p^\times$ for $0\le a<N-1$, and $v_f\in V_f\setminus\{0\}$ such that $$\rho_f(u)v_f=\psi_f\left(\sum_{a=0}^{N-2}c_{f,a}u_{a,a+1}\right)v_f$$ for every upper unitriangular matrix $u\in\mathrm{GL}_N(\mathbb F_p)$. Matrix indices run from $0$ to $N-1$; when $N=1$ the sum is empty.
