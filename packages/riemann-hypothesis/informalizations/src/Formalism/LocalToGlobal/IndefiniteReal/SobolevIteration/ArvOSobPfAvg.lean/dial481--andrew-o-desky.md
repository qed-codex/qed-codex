---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/SobolevIteration/ArvOSobPfAvg.lean",
  "declarations": [
    "Formalism.IndefR.Tow.SobPf.avgSmooth_of"
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

## Smooth vectors and integration over a compact subgroup

[Theorem REP.1480](https://andrewodesky.com/rh/lean/Formalism.IndefR.Tow.SobPf.avgSmooth_of/)

Assume the following local chart property for every pair of complex matrices $G,s$ with $s^2=1$, $s^*Gs=G$ and $Gs$ positive definite: finitely many $Y_i$ in $\mathfrak g=\{X:X^*G+GX=0\}$ give products $\prod_i\exp(t_iY_i)$ covering some identity neighborhood with arbitrarily small real parameters $t_i$. Fix such $G,s$, put $U(G)=\{g:g^*Gg=G\}$, and let $K$ be its subgroup commuting with $s$. Let $\pi$ be a strongly continuous unitary representation of this matrix group on a complex Hilbert space, and let $\mu$ be a probability measure on the ambient matrix space, supported on $K$, left invariant by $K$, and positive on every open set meeting $K$.

Let $p$ be a continuous complex-valued function on the ambient matrix space and let $w$ be a smooth vector. Then $$w_p=\int_Kp(k)\pi(k)w\,d\mu(k)$$ is smooth. For every list $X_1,\ldots,X_r\in\mathfrak g$, the differentiated integrand is integrable and $$d\pi(X_1)\cdots d\pi(X_r)w_p =\int_Kp(k)d\pi(X_1)\cdots d\pi(X_r)(\pi(k)w)\,d\mu(k).$$
