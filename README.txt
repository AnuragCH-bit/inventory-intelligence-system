# Inventory Intelligence System

## Dataset Design

### Categories
- Bearing
- Seal
- Filter
- Electrical
- Fastener
- Chemical
- Raw Metal
- Consumable

### Embedded Patterns

1. Seasonal Demand
   - Filters increase during Apr-Aug
   - Chemicals increase during Jun-Sep

2. Unreliable Supplier
   - SUP-013
   - High lead time variability
   - Low reliability score

3. Critical Stockout SKUs
   - BRG-0005
   - SEA-0015
   - ELE-0012

### Datasets Generated

- parts_master.csv
- suppliers.csv
- inventory_snapshot.csv
- consumption_logs.csv
- purchase_orders.csv