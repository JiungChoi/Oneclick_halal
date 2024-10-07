# 1. Notation

Item master : Item의 가격, 이미지, 재고 등을 관리하는 정보

# 2. Item Master Manager

Item Master Manager는 Item Master에 대한 정보를 관리하는 클래스입니다.

외부 요청에 따라 Item Master를 저장하고, 저장된 Item Master를 반환해주는 서비스입니다.

# 3. GraphQL APIs

### 3.1 Endpoints

```
/graphql
```

### 3.2 Models

```python
# ItemMaster
class ItemMasterInput:
    id: str
    price: int
    image_path: str
    total_quantity: int
    onhand_quantity: int
    available_quantity: int

class ItemMasterOutput:
    id: str
    price: int
    image_path: str
    total_quantity: int
    onhand_quantity: int
    available_quantity: int
```

### 3.3 Queries

```
[✅] itemMaster(id: String!): ItemMasterOutput
[✅] itemMasters(
        limit: Int! = 10
        offset: Int! = 0
        sortBy: String = null
        sortOrder: String! = "asc"
     ): [ItemMasterOutput!]!
     - sortOrder ("asc" or "desc")
```

- Example

```graphql
# itemMaster
{
	itemMaster(id: "I001") {
    id
    price
    image_path
    total_quantity
    onhand_quantity
    available_quantity
  }
}

# itemMasters
{
  itemMasters(
    limit: 10, 
    offset: 0,
  ) {
    price
    image_path
    total_quantity
    onhand_quantity
    available_quantity
  }
}

```



### 3.4 Mutations

```
[✅] createItemMaster(itemMaster: ItemMasterInput!): ItemMasterOutput!
[✅] updateItemMaster(itemMaster: ItemMasterInput!): ItemMasterOutput!
```

- Example

```graphql
# createItemMaster
mutation{
  createItemMaster(itemMaster: {
    id: "I001"
    price: 2000
    image_path: "https://oneclick-halal/images/item001.png"
    total_quantity: 10
    onhand_quantity: 5
    available_quantity: 0
  })
  {
    id
    price
    image_path
    total_quantity
    onhand_quantity
    available_quantity
  }
}
# updateItemMaster
mutation{
  updateItemMaster(itemMaster: {
    id: "I001"
    price: 2500
    image_path: "https://oneclick-halal/images/item001.png" 
    total_quantity: 10
    onhand_quantity: 5
    available_quantity: 0
  })
  {
    id
    price
    image_path
    total_quantity
    onhand_quantity
    available_quantity
  }
}
```
