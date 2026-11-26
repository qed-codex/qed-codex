---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/TorsionTranslationPowers/ShiftAnalyticW.lean",
  "declarations": [
    "Formalism.L2.Th1.E.ptWAdd",
    "Formalism.L2.Th1.E.shiftAnalyticW"
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

## Additivity of transported Weierstrass uniformization

[Theorem AV.0906](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.E.ptWAdd/)

Let $\ell$ be prime, $L$ an elliptic period pair with lattice $\Lambda\subseteq\mathbb C$, and $\iota:\mathbb C\simeq\mathbb C_\ell$ a field isomorphism. Let $W$ be a Weierstrass curve over $\mathbb C_\ell$ with $$c_4(W)/12=\iota(g_2(L)),\qquad c_6(W)/216=\iota(g_3(L)).$$ For $z\notin\Lambda$, put $$x(z)=\iota(\wp_L(z))-b_2(W)/12,\qquad y(z)=\bigl(\iota(\wp'_L(z))-a_1(W)x(z)-a_3(W)\bigr)/2.$$ Define $P(z)$ to be the nonsingular affine point $(x(z),y(z))$ when it is such a point and $z\notin\Lambda$, and the identity otherwise. Then $$P(s+t)=P(s)+P(t)\qquad(s,t\in\mathbb C).$$

## Integral Gauss norm for prime-to-p translates of a normalized theta function

[Theorem PHT.0943](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.E.shiftAnalyticW/)

Let $\ell$ be prime, let $\mathbb C_\ell$ be the completion of an algebraic closure of $\mathbb Q_\ell$, and let $\iota:\mathbb C\simeq\mathbb C_\ell$ be a field isomorphism. Let $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\subset\mathbb C$, where $\omega_1,\omega_2$ are linearly independent over $\mathbb R$. Let $W/\mathbb C_\ell$ be a Weierstrass curve with $$\frac{c_4(W)}{12}=\iota(g_2(\Lambda)),\qquad \frac{c_6(W)}{216}=\iota(g_3(\Lambda)).$$ Suppose its five Weierstrass coefficients have norm at most one and $|\Delta(W)|_\ell=1$.

Use the operators $U_s$ of ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)) and the transformation $\mathcal T_{\iota,W}$ of ([Formal logarithms and Taylor expansions for Weierstrass curves](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.A.logSer/)). Choose $\omega_0\in\Lambda$ with $t=\omega_0/2\notin\Lambda$, and let $\theta_t$ be the function defined in ([A normalized even theta function at a half period](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.th0Basic/)). Suppose $$\left|\iota(\wp_\Lambda(t))-\frac{b_2(W)}{12}\right|_\ell\le1.$$ Writing $\mathcal T_{\iota,W}(\theta_t)=\sum_{n\ge0}a_nT^n$, suppose also that $a_0=1$ and $|a_n|_\ell\le1$ for every $n\ge0$.

For every $s\in\mathbb C$ such that $Ns\in\Lambda$ for some positive integer $N$ not divisible by $\ell$, write $$\mathcal T_{\iota,W}(U_s\theta_t)=\sum_{n\ge0}b_nT^n.$$ Then $|b_n|_\ell\le1$ for every $n\ge0$, and $|b_m|_\ell=1$ for some nonnegative integer $m$.
