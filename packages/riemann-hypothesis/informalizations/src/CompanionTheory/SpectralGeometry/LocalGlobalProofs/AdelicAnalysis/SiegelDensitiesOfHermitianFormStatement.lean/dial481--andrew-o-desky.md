---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/SiegelDensitiesOfHermitianFormStatement.lean",
  "declarations": [
    "GlobalTheory.T.siegel_densities_of_hermitian_form"
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

## A product formula for averaged representation counts

[Theorem THETA.1727](https://andrewodesky.com/rh/lean/GlobalTheory.T.siegel_densities_of_hermitian_form/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J$ be a nondegenerate $\sigma$-Hermitian form on $E^M$. Let $n\ge0$ satisfy $2n<M$, and let $T\in\operatorname{Herm}_n(E)$ have nonzero determinant. Choose an $F$-basis $b$ of $E$ and a test function $\Phi=\Phi_\infty\Phi_f$ on $(\mathbb A_F\otimes_F E)^{nM}$. Assume $\Phi_\infty$ is continuous, smooth and compactly supported in every real linear coordinate system, and rapidly decreasing with respect to the sum of absolute values of its $b$-coordinates. Assume $\Phi_f=\prod_v\Phi_v$, with every $\Phi_v$ locally constant and compactly supported and, at all but finitely many $v$, equal to the indicator of the integral coordinate lattice defined by $b$.

Write $H=U(J)$ and $q(X)=(J(X_a,X_b))_{a,b}$ for the Gram map on $n$-tuples. Haar measures on $H(\mathbb A_F)$, fundamental domains $\mathcal F$ for $H(F)$, and continuous unitary nontrivial additive characters $\psi$ of $\mathbb A_F/F$ exist. For every such choice, self-dual additive Haar measures $\mu_u$ on the tuple spaces and $\nu_u$ on the Hermitian matrix spaces exist, at $u=\infty$ and at every finite place. Their pairings are respectively $$\psi_u\!\left(\sum_a\operatorname{Tr}_{E_u/F_u}J(X_a,Y_a)\right),\qquad \psi_u\!\left(\tfrac12\operatorname{Tr}_{E_u/F_u}\operatorname{tr}(ST)\right),$$ with $E_u=F_u\otimes_F E$ and the corresponding product algebras at infinity.

For every such system of self-dual measures there are functions $g_\infty,g_v$ on the local Hermitian spaces, continuous on the locus of invertible matrices, such that for every compact set $B$ in that locus, $$\int_{q^{-1}(B)}\Phi_u(X)\,d\mu_u(X)=\int_Bg_u(S)\,d\nu_u(S).$$ The product $\prod_vg_v(T)$ converges, and $$v_\mu(\mathcal F)^{-1}\int_{\mathcal F}\sum_{\substack{X\in(E^M)^n\\q(X)=T}}\Phi(h^{-1}X)\,d\mu(h) =g_\infty(T)\prod_vg_v(T).$$ Here $v_\mu(\mathcal F)$ is the real-valued volume: it equals $\mu(\mathcal F)$ when finite and is defined to be zero otherwise, with inverse zero at zero.
