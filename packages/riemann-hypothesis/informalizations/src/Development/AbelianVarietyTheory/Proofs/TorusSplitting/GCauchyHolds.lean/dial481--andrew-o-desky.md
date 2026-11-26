---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TorusSplitting/GCauchyHolds.lean",
  "declarations": [
    "GlobalTheory.ThetaTorus.J_holds",
    "GlobalTheory.ThetaTorus.N_holds"
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

## A lower bound for a determinant derivative of a normalized theta section

[Theorem THETA.0059](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaTorus.J_holds/)

Let $E$ be a CM number field, $f=[E:\mathbb Q]/2$ and $\delta=|\operatorname{disc}E|^{1/[E:\mathbb Q]}$. Fix the polarized torus data $(V,\Lambda,\epsilon,r,(d_\tau))$ described below, and put $g=\dim_{\mathbb C}V=fr$. Let $n\ge0$. For each of finitely many blocks $b$, choose an embedding $\tau_b$, an integer $0\le i_b\le d_{\tau_b}$, an integer $c_b\ge1$ and an injection $\gamma_b:\{1,\ldots,i_b\}\to\{1,\ldots,n\}$. Require different blocks to use disjoint column sets. Define $$P(X)=\prod_b\det\bigl(X_{\gamma_b(v),\tau_b,u}\bigr)_{1\le u,v\le i_b}^{c_b},\qquad D=\sum_b i_bc_b.$$ Choose $q,m\in\mathbb N$, $R_0\in\mathbb R$, and put $$R=\delta^7,\quad d_*=2fm,\quad\theta=\sqrt{fR_0^2R^3/q},\quad b_0=\frac q{R_0^2R^4},\quad t_0=qb_0,$$ $$M_1=90m^2d_*^2\delta,\quad\omega_*=2f^{3/2}\delta,\quad C_\chi=8100m^4d_*^4R.$$ Assume all the parameter conditions below. Let $\lambda_1=\inf\{\|x\|:0\ne x\in\Lambda\}$ and put $$\Phi=\begin{cases}2f/(\delta^2\lambda_1^2),&\lambda_1<\theta,\\0,&\lambda_1\ge\theta.\end{cases}$$ There is an entire theta section $F:V^n\to\mathbb C$ of level $q$, with normalized squared $L^2$ norm one, such that $$|P(\partial)F(0)|^2\ge4^{-n}\bigl(6(2d_*)^{d_*/2}\bigr)^{-n}2^{-(r+2)D}\exp(-2\pi nC_\chi\Phi/q).$$

## Orthogonal spanning theta translates on a polarized torus

[Theorem AV.0853](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaTorus.N_holds/)

Let $E$ be a CM number field and choose nonnegative integers $d_\tau$ indexed by its complex embeddings, with $d_\tau+d_{\bar\tau}=r$ for one integer $r\ge0$. Put $$V=\bigoplus_{\tau:E\hookrightarrow\mathbb C}\mathbb C^{d_\tau},\qquad H(v,w)=\sum_{\tau,j}v_{\tau,j}\overline{w_{\tau,j}},$$ and let $\mathcal O_E$ act on the $\tau$-coordinates through $\tau$. Fix a real basis of $V$ and let $\Lambda$ be its integral span. Assume $\Lambda$ is $\mathcal O_E$-stable and $\operatorname{Im}H$ is integral and perfect on $\Lambda$. Choose $\epsilon:\Lambda\to\{\pm1\}$ with $$\epsilon(x+y)=\epsilon(x)\epsilon(y)(-1)^{\operatorname{Im}H(x,y)},$$ and require $\epsilon(x)=1$ whenever $\operatorname{Im}H(\alpha x,x)=0$ for every $\alpha\in\mathcal O_E$.

Let $q\ge1$, $n\ge0$, and let $\Pi:V\to V$ be complex-linear, commute with $\mathcal O_E$, preserve $\Lambda$, and satisfy $$H(\Pi v,\Pi w)=qH(v,w),\qquad \epsilon(\Pi x)=\epsilon(x)^q\quad(x\in\Lambda).$$ Let $0\ne s\in\Theta_{1,1}$, with $\Theta_{q,n}$ defined below. Let $K\subseteq V^n$ be finite, with $qb_i\in\Lambda$ for every $b\in K$, and suppose every $b\in(q^{-1}\Lambda)^n$ has a unique $b'\in K$ with $\Pi(b_i-b'_i)\in\Lambda$ for every $i$.

Put $S(v)=\prod_{i=1}^ns(\Pi v_i)$ and $$S_b(v)=\exp\left(q\pi\sum_iH(v_i,b_i)-\frac{q\pi}2\sum_iH(b_i,b_i)\right)S(v-b).$$ Then the $S_b$ belong to $\Theta_{q,n}$, span it, and are pairwise orthogonal for the pairing below. Each has squared norm $$\|S_b\|_q^2=\|s\|_1^{2n}.$$
