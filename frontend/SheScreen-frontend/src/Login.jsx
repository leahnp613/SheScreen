export default function Login() {
  return (
    <>
      <div className="form">
        <div className="form__content">
          <p className="form__welcome">Welcome back!</p>
          <p className="form__title">Please sign in to resume your journey</p>

          <input
            type="email"
            className="form__input"
            placeholder="Email Address"
            id="email"
            required
          />

          <input
            type="password"
            className="form__input"
            placeholder="Password"
            id="password"
            required
          />
          <button className="btn">Login</button>
        </div>
      </div>
    </>
  );
}
