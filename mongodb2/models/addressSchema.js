/* @flow */

import { Schema } from 'mongoose';

export const AddressSchema: Schema<any> = new Schema(
  {
    street: String,
    city: String,
    region: String,
    postalCode: String,
    country: String,
    phone: String,
  },
  {
    _id: false,
  }
);
