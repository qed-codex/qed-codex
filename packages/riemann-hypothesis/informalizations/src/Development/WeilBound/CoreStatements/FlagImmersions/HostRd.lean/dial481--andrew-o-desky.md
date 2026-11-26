---
{
  "module": "src/Development/WeilBound/CoreStatements/FlagImmersions/HostRd.lean",
  "declarations": [
    "RootFieldNumerics.RF.chiEx"
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

## A quadratic character giving the prescribed CM period expression

[Theorem ANT.1103](https://andrewodesky.com/rh/lean/RootFieldNumerics.RF.chiEx/)

Let $E$ be a CM number field and fix the following arithmetic datum. Let $d\equiv7\pmod{16}$ be prime, $r,w\in\mathcal O_E$ with $r^2=-d$ and $2w=1+r$, the integral involution induced by complex conjugation, and a complex number $r_0$ with $r_0^2=-d$. Assume $E/E^+$ is unramified at all finite places. Let $\chi_d$ be the quadratic character modulo $d$ obtained from the quadratic character of $\mathbb F_d$, and put $$\mathcal L_d=\operatorname{Re}\frac{L'(1,\chi_d)}{L(1,\chi_d)},\qquad \mathrm{rd}_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]}.$$ There is a Dirichlet character $\chi$ modulo $d$ such that $\chi(n)=\left(\frac{-d}{n}\right)$ for every positive odd integer $n$, with the Jacobi-symbol convention also covering $n=1$, and $$\operatorname{Re}\left(\gamma+\log\frac{2\pi}{\mathrm{rd}_E}-\frac{L'(1,\chi)}{L(1,\chi)}\right)=\gamma+\log(2\pi)-\log\mathrm{rd}_E-\mathcal L_d.$$ Here $\gamma$ is Euler's constant.
