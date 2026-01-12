# Réservation de Salles

This project is a custom Odoo module designed to manage room reservations. It allows users to book rooms, specify time slots, and track the status of reservations.

## Features

- **Room Booking**: Reserve a room by specifying its name.
- **Scheduling**: Set the reservation date, start time, and end time.
- **Responsibility**: Assign a responsible user for the reservation (defaults to the logged-in user).
- **Status Workflow**: Track the state of the reservation:
  - **Draft** (`Brouillon`): Initial state.
  - **Confirmed** (`Confirmée`): Reservation is approved/active.
  - **Cancelled** (`Annulée`): Reservation is no longer valid.

## Structure

The project is structured as a Dockerized Odoo environment containing the custom addon.

- **addons/reservation_salles**: The main module directory.
  - **models/reservation.py**: Defines the `reservation.salle` data model.
  - **views/reservation_views.xml**: Contains the UI definitions (lists, forms).
  - **security**: Access control rules.
- **docker-compose.yml**: Configuration to run Odoo 17 and PostgreSQL 15 containers.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd odoo_reservation_salles
   ```

2. **Start the containers:**
   Run the following command to start Odoo and the database in the background:
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo:**
   Open your browser and navigate to:
   [http://localhost:8069](http://localhost:8069)

   **Default Database Credentials** (as defined in `docker-compose.yml`):
   - **Email/User**: `odoo` (or `admin` depending on initial setup compatibility)
   - **Password**: `odoo`
   - **Database User**: `odoo`
   - **Database Password**: `odoo`

4. **Install the Module:**
   - Log in to Odoo.
   - Go to **Apps**.
   - Click "Update Apps List" (you may need to enable Developer Mode first or remove the 'Apps' filter).
   - Search for **Réservation de Salles**.
   - Click **Activate** to install the module.

## Usage

Once installed, you should see a new menu item or application for **Réservation de Salles** (depending on the menu configuration). You can create new reservations, set the date and time, and manage the reservation status.
