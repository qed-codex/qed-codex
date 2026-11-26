---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRationalFormalPathOfIntegralAllPlacesStatement.lean",
  "declarations": [
    "GlobalTheory.T.isRationalFormalPath_of_integral_allPlaces"
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

## Rationality of a formal path integral at all places

[Theorem AG.1546](https://andrewodesky.com/rh/lean/GlobalTheory.T.isRationalFormalPath_of_integral_allPlaces/)

Let $k$ be algebraically closed of characteristic zero, let $K/k$ be a field extension, and let $E/K$ be finite with the compatible $k$-algebra structures. Let $C/k$ be smooth, projective and geometrically connected of relative dimension one, and let $x:\operatorname{Spec}K\to C$ be a dominant preimmersion over $k$. Let $G/C$ be a group scheme and $\xi:\operatorname{Spec}E[[T]]\to G$. For each $k$-place $p$ of $E$, choose $u_p\in E^\times$ with $$\{p:\operatorname{ord}_p(u_p)\ne0\}\text{ finite},\qquad\sum_p\operatorname{ord}_p(u_p)>0.$$ Suppose for every $p$ there are $b_p:\operatorname{Spec}\mathcal O_p\to C$ extending $x$ after passing to $E$, and $\zeta_p:\operatorname{Spec}\mathcal O_p[[T]]\to G$ over $b_p$, such that $$\zeta_p(0)=e(b_p),\qquad\zeta_p(2T)=[2]\zeta_p(T),\qquad\xi(T)=\zeta_p(u_pT)$$ after embedding the coefficients in $E$. Then some $\beta:\operatorname{Spec}E(T)\to G$ agrees with $\xi$ after both are pulled back to $\operatorname{Spec}E((T))$.
