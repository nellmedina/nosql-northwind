/* @flow */

import { Schema, model } from 'mongoose';
import { composeWithMongoose } from '../schemaComposer';
import { AddressSchema } from './addressSchema';
import { CustomerTC } from './customer';
import { EmployeeTC } from './employee';
import { ShipperTC } from './shipper';
import { ProductTC } from './product';

export const OrderDetailsSchema: Schema<any> = new Schema(
  {
    productID: Number,
    unitPrice: Number,
    quantity: Number,
    discount: Number,
  },
  {
    _id: false,
  }
);

export const OrderSchema: Schema<any> = new Schema(
  {
    orderID: {
      type: Number,
      description: 'Order unique ID',
      unique: true,
    },
    customerID: String,
    employeeID: Number,
    orderDate: Date,
    requiredDate: Date,
    shippedDate: Date,
    shipVia: Number,
    freight: Number,
    shipName: String,
    shipAddress: AddressSchema,
    details: {
      type: [OrderDetailsSchema],
      index: true,
      description: 'List of ordered products',
    },
  },
  {
    collection: 'northwind_orders',
  }
);

export const Order = model('Order', OrderSchema);

export const OrderTC = composeWithMongoose<any>(Order);

OrderTC.getResolver('connection').extensions = {
  complexity: ({ args, childComplexity }) => childComplexity * (args.first || args.last || 20),
};
OrderTC.getResolver('pagination').extensions = {
  complexity: ({ args, childComplexity }) => childComplexity * (args.perPage || 20),
};
OrderTC.getResolver('findMany').extensions = {
  complexity: ({ args, childComplexity }) => childComplexity * (args.limit || 1000),
};

OrderTC.addRelation('customer', {
  resolver: () => CustomerTC.getResolver('findOne'),
  prepareArgs: {
    filter: (source) => ({ customerID: source.customerID }),
    skip: null,
    sort: null,
  },
  projection: { customerID: true },
});

OrderTC.addRelation('employee', {
  resolver: () => EmployeeTC.getResolver('findOne'),
  prepareArgs: {
    filter: (source) => ({ employeeID: source.employeeID }),
    skip: null,
    sort: null,
  },
  projection: { employeeID: true },
});

OrderTC.addRelation('shipper', {
  resolver: () => ShipperTC.getResolver('findOne'),
  prepareArgs: {
    filter: (source) => ({ shipperID: source.shipVia }),
    skip: null,
    sort: null,
  },
  projection: { shipVia: true },
});

const OrderDetailsTC = OrderTC.getFieldOTC('details');
OrderDetailsTC.addRelation('product', {
  resolver: () => ProductTC.getResolver('findOne'),
  prepareArgs: {
    filter: (source) => ({ productID: source.productID }),
    skip: null,
    sort: null,
  },
  projection: { productID: true },
});
