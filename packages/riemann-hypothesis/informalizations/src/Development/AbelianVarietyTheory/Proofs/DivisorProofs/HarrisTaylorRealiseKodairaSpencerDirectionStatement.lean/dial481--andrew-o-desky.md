---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorRealiseKodairaSpencerDirectionStatement.lean",
  "declarations": [
    "GlobalTheory.T.harrisTaylor_realise_kodairaSpencer_direction"
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

## Realizing an infinitesimal Hodge-filtration variation

[Theorem AV.1219](https://andrewodesky.com/rh/lean/GlobalTheory.T.harrisTaylor_realise_kodairaSpencer_direction/)

Let $p$ be prime and fix the source's integral PEL datum and a compatible base over a commutative ring $R$. Let $N\ge3$ with $\gcd(N,p)=1$, let $k$ be algebraically closed, let $\beta:R\to k$ be a ring map, and let $o_0$ be an object of the corresponding moduli problem over $t=\operatorname{Spec}\beta$. Let $A$ be its abelian scheme, let $H$ be its de Rham realization, and let $F\subset H$ be the Hodge subspace. Write $\rho$ for its crystalline action and $Z\subset H$ for the subspace selected by the base datum and $\beta$.

Let $\varphi$ be a $k$-bilinear form represented by the Chern class of the specified polarization correspondence on $A\times A$. If $f\in\operatorname{End}_k(H)$ satisfies $$f(\rho(a)x)-\rho(a)f(x)\in F\quad(a\in O,\ x\in F),\qquad f(Z)\subset F,$$ $$\varphi(fx,y)+\varphi(x,fy)=0\quad(x,y\in F),$$ then there is an object $o'$ over $k[\epsilon]/(\epsilon^2)$ mapping to the fixed base through $t$, with a moduli morphism identifying its reduction with $o_0$, such that every $x\in F$ has a Hodge lift with expansion $x+\epsilon f(x)$ in the crystalline comparison.
