export default function UserProfileEdit() {
    return (
      <>
        <div className="form">
          <div className="form__content">
            <h2 className="form__title">My Profile</h2>

            <input
              type="text"
              className="form__input"
              placeholder="First Name"
              id="FirstName"
              required
            />

            <input
              type="text"
              className="form__input"
              placeholder="Last Name"
              id="LastName"
              required
            />

            <label className="form__label">Month & Year of Birth</label>
            <input
              type="month"
              className="form__input"
              placeholder="Month and Year of Birth"
              id="DateOfBirth"
              required
            />

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
            <button className="btn">Save</button>
          </div>
        </div>
      </>
    );
  }
