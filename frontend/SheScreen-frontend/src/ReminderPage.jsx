import React, { useState } from "react";
import { saveReminderApi } from "./api"; // Import your API function

export default function ReminderPage() {
  const [reminderDateTime, setReminderDateTime] = useState("");
  const [isReminderSaved, setReminderSaved] = useState(false);

  const handleReminderSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make an API call to save the reminder
      await saveReminderApi({ dateTime: reminderDateTime });

      // Update state to indicate the reminder is saved
      setReminderSaved(true);
    } catch (error) {
      console.error("Error saving reminder:", error);
    }
  };

  return (
    <>
      <div className="main">
        {/* Reminder Form */}
        <form onSubmit={handleReminderSubmit}>
          <label htmlFor="reminderDateTime">Set a reminder:</label>
          <input
            type="datetime-local"
            id="reminderDateTime"
            value={reminderDateTime}
            onChange={(e) => setReminderDateTime(e.target.value)}
            required
          />
          <button type="submit">Set Reminder</button>
        </form>

        {isReminderSaved && <p>Reminder saved successfully!</p>}
      </div>
    </>
  );
}
