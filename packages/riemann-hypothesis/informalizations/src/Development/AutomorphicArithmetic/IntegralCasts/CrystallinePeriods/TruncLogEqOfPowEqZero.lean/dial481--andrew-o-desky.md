---
{
  "module": "src/Development/AutomorphicArithmetic/IntegralCasts/CrystallinePeriods/TruncLogEqOfPowEqZero.lean",
  "declarations": [
    "Reformulated.AutPerF.Acris",
    "Reformulated.AutPerF.Bcris",
    "Reformulated.AutPerF.BdR",
    "Reformulated.AutPerF.BdRPlus",
    "Reformulated.AutPerF.acrisZero"
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

## Fontaine's crystalline and de Rham period rings

[Definition / hypothesis PHT.D253](https://andrewodesky.com/rh/lean/Reformulated.AutPerF.BdRPlus/)

Fontaine's period rings attach linear algebra to $\ell$-adic Galois representations by extending scalars and then taking Galois invariants. The de Rham ring carries a filtration; the crystalline ring also carries Frobenius.

Let $\ell$ be prime, let $\mathbb C_\ell$ be the completion of $\overline{\mathbb Q}_\ell$, and let $\mathcal O_{\mathbb C_\ell}$ be its valuation ring. Put $$R=\varprojlim_{x\mapsto x^\ell}\mathcal O_{\mathbb C_\ell}/\ell,\qquad A_{\mathrm{inf}}=W(R),$$ where $W(R)$ is the ring of $\ell$-typical Witt vectors of the perfect ring $R$. The ring $R$ is the tilt of $\mathcal O_{\mathbb C_\ell}$. For $x=(x_n)\in R$, define $$x^\sharp=\lim_{n\to\infty}\widetilde x_n^{\,\ell^n}\in\mathcal O_{\mathbb C_\ell},$$ where $\widetilde x_n$ is any lift of $x_n$ to $\mathcal O_{\mathbb C_\ell}$. Write $[x]\in W(R)$ for the Teichmüller lift: the multiplicative representative of $x$ modulo $\ell$. Fontaine's homomorphism is $$\Theta:A_{\mathrm{inf}}\longrightarrow\mathcal O_{\mathbb C_\ell},\qquad \Theta\left(\sum_{n\ge0}\ell^n[y_n]\right)=\sum_{n\ge0}\ell^n y_n^\sharp\qquad(y_n\in R).$$ Let $I=\ker(\Theta:A_{\mathrm{inf}}[1/\ell]\to\mathbb C_\ell)$, using the extension of $\Theta$ after inverting $\ell$. Define $$B_{\mathrm{dR}}^+=\varprojlim_{m\ge1} A_{\mathrm{inf}}[1/\ell]/I^m,\qquad B_{\mathrm{dR}}=\operatorname{Frac}(B_{\mathrm{dR}}^+).$$ The projection at $m=1$, followed by the map induced by $\Theta$, is the residue map $\Theta_{\mathrm{dR}}:B_{\mathrm{dR}}^+\to\mathbb C_\ell$.

Choose roots of unity $\zeta_n\in\overline{\mathbb Q}_\ell$ with $\zeta_0=1$, $\zeta_1\ne1$, and $\zeta_{n+1}^\ell=\zeta_n$. Put $\epsilon=(\zeta_n\bmod\ell)_{n\ge0}\in R$ and $t=\log[\epsilon]$, where $$\log[\epsilon]=\sum_{n\ge1}\frac{(-1)^{n+1}}{n}([\epsilon]-1)^n.$$ This series converges in $B_{\mathrm{dR}}^+$. Its value generates $\ker\Theta_{\mathrm{dR}}$, and the filtration is $$\operatorname{Fil}^hB_{\mathrm{dR}}=t^hB_{\mathrm{dR}}^+\qquad(h\in\mathbb Z).$$ In particular, $\operatorname{Fil}^0B_{\mathrm{dR}}=B_{\mathrm{dR}}^+$. Algebraic scalars embed as follows: a $\mathbb Q_\ell$-embedding $j:F\to\mathbb C_\ell$ of an algebraic extension $F/\mathbb Q_\ell$ has a unique $\mathbb Q_\ell$-algebra lift $s:F\to B_{\mathrm{dR}}^+$ satisfying $\Theta_{\mathrm{dR}}\circ s=j$.

For the crystalline ring, form the subalgebra $$A_{\mathrm{cris}}^0=A_{\mathrm{inf}}\left[\frac{x^n}{n!}:x\in\ker(\Theta:A_{\mathrm{inf}}\to\mathcal O_{\mathbb C_\ell}),\ n\ge0\right]\subset A_{\mathrm{inf}}[1/\ell].$$ Define $A_{\mathrm{cris}}$ to be its $\ell$-adic completion and put $$B_{\mathrm{cris}}^+=A_{\mathrm{cris}}[1/\ell],\qquad B_{\mathrm{cris}}=B_{\mathrm{cris}}^+[1/t].$$ The logarithmic series defining $t$ also converges $\ell$-adically in $A_{\mathrm{cris}}$. The compatible maps from $A_{\mathrm{inf}}$ induce a homomorphism $\iota_{\mathrm{cris}}:B_{\mathrm{cris}}\to B_{\mathrm{dR}}$ taking this $t$ to $\log[\epsilon]$. The crystalline filtration is $$\operatorname{Fil}^hB_{\mathrm{cris}}=\iota_{\mathrm{cris}}^{-1}(\operatorname{Fil}^hB_{\mathrm{dR}}).$$

The action of $G_{\mathbb Q_\ell}=\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell)$ on $\mathbb C_\ell$ induces actions on the tilt, Witt vectors and these completions and localizations. These actions commute with $\iota_{\mathrm{cris}}$ and preserve the filtration. The Witt-vector Frobenius, specified by $\Phi([x])=[x^\ell]$ and $\Phi(\ell)=\ell$, extends to $B_{\mathrm{cris}}$, commutes with the Galois action, and satisfies $\Phi(t)=\ell t$. For the cyclotomic character $\chi_\ell:G_{\mathbb Q_\ell}\to\mathbb Z_\ell^\times$, characterized by $g(\zeta_n)=\zeta_n^{\chi_\ell(g)\bmod\ell^n}$, one has $g(t)=\chi_\ell(g)t$.
