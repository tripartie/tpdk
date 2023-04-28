<?php
/**
 * OfferUpdate
 *
 * PHP version 7.4
 *
 * @category Class
 * @package  Tripartie\Tpdk
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * Tripartie
 *
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.0.b1
 * Contact: noc@tripartie.com
 * Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 6.5.0
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace Tripartie\Tpdk\Model;

use \ArrayAccess;
use \Tripartie\Tpdk\ObjectSerializer;

/**
 * OfferUpdate Class Doc Comment
 *
 * @category Class
 * @description 
 * @package  Tripartie\Tpdk
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 * @implements \ArrayAccess<string, mixed>
 */
class OfferUpdate implements ModelInterface, ArrayAccess, \JsonSerializable
{
    public const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'Offer-Update';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'publicUrl' => 'string',
        'enforcePersonaAuth' => 'bool',
        'overrideRateCommissionSafeCheckout' => 'float',
        'redirectUrl' => 'string',
        'title' => 'string',
        'description' => 'string',
        'unitPrice' => 'float',
        'currencyCode' => 'string',
        'itemCount' => 'int',
        'weightInGram' => 'int',
        'shippingAllowed' => 'bool',
        'handDeliveryAllowed' => 'bool',
        'shippingCarriers' => 'string[]',
        'eanCode' => 'string',
        'metadata' => '\Tripartie\Tpdk\Model\MetadataUpdate[]'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      * @phpstan-var array<string, string|null>
      * @psalm-var array<string, string|null>
      */
    protected static $openAPIFormats = [
        'publicUrl' => null,
        'enforcePersonaAuth' => null,
        'overrideRateCommissionSafeCheckout' => null,
        'redirectUrl' => null,
        'title' => null,
        'description' => null,
        'unitPrice' => null,
        'currencyCode' => null,
        'itemCount' => null,
        'weightInGram' => null,
        'shippingAllowed' => null,
        'handDeliveryAllowed' => null,
        'shippingCarriers' => null,
        'eanCode' => null,
        'metadata' => null
    ];

    /**
      * Array of nullable properties. Used for (de)serialization
      *
      * @var boolean[]
      */
    protected static array $openAPINullables = [
        'publicUrl' => true,
		'enforcePersonaAuth' => false,
		'overrideRateCommissionSafeCheckout' => false,
		'redirectUrl' => true,
		'title' => false,
		'description' => true,
		'unitPrice' => true,
		'currencyCode' => true,
		'itemCount' => false,
		'weightInGram' => true,
		'shippingAllowed' => false,
		'handDeliveryAllowed' => false,
		'shippingCarriers' => false,
		'eanCode' => true,
		'metadata' => false
    ];

    /**
      * If a nullable field gets set to null, insert it here
      *
      * @var boolean[]
      */
    protected array $openAPINullablesSetToNull = [];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of nullable properties
     *
     * @return array
     */
    protected static function openAPINullables(): array
    {
        return self::$openAPINullables;
    }

    /**
     * Array of nullable field names deliberately set to null
     *
     * @return boolean[]
     */
    private function getOpenAPINullablesSetToNull(): array
    {
        return $this->openAPINullablesSetToNull;
    }

    /**
     * Setter - Array of nullable field names deliberately set to null
     *
     * @param boolean[] $openAPINullablesSetToNull
     */
    private function setOpenAPINullablesSetToNull(array $openAPINullablesSetToNull): void
    {
        $this->openAPINullablesSetToNull = $openAPINullablesSetToNull;
    }

    /**
     * Checks if a property is nullable
     *
     * @param string $property
     * @return bool
     */
    public static function isNullable(string $property): bool
    {
        return self::openAPINullables()[$property] ?? false;
    }

    /**
     * Checks if a nullable property is set to null.
     *
     * @param string $property
     * @return bool
     */
    public function isNullableSetToNull(string $property): bool
    {
        return in_array($property, $this->getOpenAPINullablesSetToNull(), true);
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'publicUrl' => 'publicUrl',
        'enforcePersonaAuth' => 'enforcePersonaAuth',
        'overrideRateCommissionSafeCheckout' => 'overrideRateCommissionSafeCheckout',
        'redirectUrl' => 'redirectUrl',
        'title' => 'title',
        'description' => 'description',
        'unitPrice' => 'unitPrice',
        'currencyCode' => 'currencyCode',
        'itemCount' => 'itemCount',
        'weightInGram' => 'weightInGram',
        'shippingAllowed' => 'shippingAllowed',
        'handDeliveryAllowed' => 'handDeliveryAllowed',
        'shippingCarriers' => 'shippingCarriers',
        'eanCode' => 'eanCode',
        'metadata' => 'metadata'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'publicUrl' => 'setPublicUrl',
        'enforcePersonaAuth' => 'setEnforcePersonaAuth',
        'overrideRateCommissionSafeCheckout' => 'setOverrideRateCommissionSafeCheckout',
        'redirectUrl' => 'setRedirectUrl',
        'title' => 'setTitle',
        'description' => 'setDescription',
        'unitPrice' => 'setUnitPrice',
        'currencyCode' => 'setCurrencyCode',
        'itemCount' => 'setItemCount',
        'weightInGram' => 'setWeightInGram',
        'shippingAllowed' => 'setShippingAllowed',
        'handDeliveryAllowed' => 'setHandDeliveryAllowed',
        'shippingCarriers' => 'setShippingCarriers',
        'eanCode' => 'setEanCode',
        'metadata' => 'setMetadata'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'publicUrl' => 'getPublicUrl',
        'enforcePersonaAuth' => 'getEnforcePersonaAuth',
        'overrideRateCommissionSafeCheckout' => 'getOverrideRateCommissionSafeCheckout',
        'redirectUrl' => 'getRedirectUrl',
        'title' => 'getTitle',
        'description' => 'getDescription',
        'unitPrice' => 'getUnitPrice',
        'currencyCode' => 'getCurrencyCode',
        'itemCount' => 'getItemCount',
        'weightInGram' => 'getWeightInGram',
        'shippingAllowed' => 'getShippingAllowed',
        'handDeliveryAllowed' => 'getHandDeliveryAllowed',
        'shippingCarriers' => 'getShippingCarriers',
        'eanCode' => 'getEanCode',
        'metadata' => 'getMetadata'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }

    public const SHIPPING_CARRIERS_SWISS_POST = 'SwissPost';
    public const SHIPPING_CARRIERS_COLISSIMO = 'Colissimo';
    public const SHIPPING_CARRIERS_MONDIAL_RELAY = 'MondialRelay';

    /**
     * Gets allowable values of the enum
     *
     * @return string[]
     */
    public function getShippingCarriersAllowableValues()
    {
        return [
            self::SHIPPING_CARRIERS_SWISS_POST,
            self::SHIPPING_CARRIERS_COLISSIMO,
            self::SHIPPING_CARRIERS_MONDIAL_RELAY,
        ];
    }

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->setIfExists('publicUrl', $data ?? [], null);
        $this->setIfExists('enforcePersonaAuth', $data ?? [], null);
        $this->setIfExists('overrideRateCommissionSafeCheckout', $data ?? [], null);
        $this->setIfExists('redirectUrl', $data ?? [], null);
        $this->setIfExists('title', $data ?? [], null);
        $this->setIfExists('description', $data ?? [], null);
        $this->setIfExists('unitPrice', $data ?? [], null);
        $this->setIfExists('currencyCode', $data ?? [], 'EUR');
        $this->setIfExists('itemCount', $data ?? [], 1);
        $this->setIfExists('weightInGram', $data ?? [], null);
        $this->setIfExists('shippingAllowed', $data ?? [], null);
        $this->setIfExists('handDeliveryAllowed', $data ?? [], true);
        $this->setIfExists('shippingCarriers', $data ?? [], null);
        $this->setIfExists('eanCode', $data ?? [], null);
        $this->setIfExists('metadata', $data ?? [], null);
    }

    /**
    * Sets $this->container[$variableName] to the given data or to the given default Value; if $variableName
    * is nullable and its value is set to null in the $fields array, then mark it as "set to null" in the
    * $this->openAPINullablesSetToNull array
    *
    * @param string $variableName
    * @param array  $fields
    * @param mixed  $defaultValue
    */
    private function setIfExists(string $variableName, array $fields, $defaultValue): void
    {
        if (self::isNullable($variableName) && array_key_exists($variableName, $fields) && is_null($fields[$variableName])) {
            $this->openAPINullablesSetToNull[] = $variableName;
        }

        $this->container[$variableName] = $fields[$variableName] ?? $defaultValue;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['enforcePersonaAuth'] === null) {
            $invalidProperties[] = "'enforcePersonaAuth' can't be null";
        }
        if ($this->container['overrideRateCommissionSafeCheckout'] === null) {
            $invalidProperties[] = "'overrideRateCommissionSafeCheckout' can't be null";
        }
        if ($this->container['itemCount'] === null) {
            $invalidProperties[] = "'itemCount' can't be null";
        }
        if ($this->container['shippingAllowed'] === null) {
            $invalidProperties[] = "'shippingAllowed' can't be null";
        }
        if ($this->container['handDeliveryAllowed'] === null) {
            $invalidProperties[] = "'handDeliveryAllowed' can't be null";
        }
        if ($this->container['shippingCarriers'] === null) {
            $invalidProperties[] = "'shippingCarriers' can't be null";
        }
        if ($this->container['metadata'] === null) {
            $invalidProperties[] = "'metadata' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets publicUrl
     *
     * @return string|null
     */
    public function getPublicUrl()
    {
        return $this->container['publicUrl'];
    }

    /**
     * Sets publicUrl
     *
     * @param string|null $publicUrl If specified, there would be not need for you to fill-in details. Must be accessible over WAN.
     *
     * @return self
     */
    public function setPublicUrl($publicUrl)
    {
        if (is_null($publicUrl)) {
            array_push($this->openAPINullablesSetToNull, 'publicUrl');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('publicUrl', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['publicUrl'] = $publicUrl;

        return $this;
    }

    /**
     * Gets enforcePersonaAuth
     *
     * @return bool
     */
    public function getEnforcePersonaAuth()
    {
        return $this->container['enforcePersonaAuth'];
    }

    /**
     * Sets enforcePersonaAuth
     *
     * @param bool $enforcePersonaAuth Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration.
     *
     * @return self
     */
    public function setEnforcePersonaAuth($enforcePersonaAuth)
    {
        if (is_null($enforcePersonaAuth)) {
            throw new \InvalidArgumentException('non-nullable enforcePersonaAuth cannot be null');
        }
        $this->container['enforcePersonaAuth'] = $enforcePersonaAuth;

        return $this;
    }

    /**
     * Gets overrideRateCommissionSafeCheckout
     *
     * @return float
     */
    public function getOverrideRateCommissionSafeCheckout()
    {
        return $this->container['overrideRateCommissionSafeCheckout'];
    }

    /**
     * Sets overrideRateCommissionSafeCheckout
     *
     * @param float $overrideRateCommissionSafeCheckout Override YOUR platform fees for that particular Offer.
     *
     * @return self
     */
    public function setOverrideRateCommissionSafeCheckout($overrideRateCommissionSafeCheckout)
    {
        if (is_null($overrideRateCommissionSafeCheckout)) {
            throw new \InvalidArgumentException('non-nullable overrideRateCommissionSafeCheckout cannot be null');
        }
        $this->container['overrideRateCommissionSafeCheckout'] = $overrideRateCommissionSafeCheckout;

        return $this;
    }

    /**
     * Gets redirectUrl
     *
     * @return string|null
     */
    public function getRedirectUrl()
    {
        return $this->container['redirectUrl'];
    }

    /**
     * Sets redirectUrl
     *
     * @param string|null $redirectUrl Fill-in that field IF you intend to redirect your customer instead of using a WebView.
     *
     * @return self
     */
    public function setRedirectUrl($redirectUrl)
    {
        if (is_null($redirectUrl)) {
            array_push($this->openAPINullablesSetToNull, 'redirectUrl');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('redirectUrl', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['redirectUrl'] = $redirectUrl;

        return $this;
    }

    /**
     * Gets title
     *
     * @return string|null
     */
    public function getTitle()
    {
        return $this->container['title'];
    }

    /**
     * Sets title
     *
     * @param string|null $title title
     *
     * @return self
     */
    public function setTitle($title)
    {
        if (is_null($title)) {
            throw new \InvalidArgumentException('non-nullable title cannot be null');
        }
        $this->container['title'] = $title;

        return $this;
    }

    /**
     * Gets description
     *
     * @return string|null
     */
    public function getDescription()
    {
        return $this->container['description'];
    }

    /**
     * Sets description
     *
     * @param string|null $description description
     *
     * @return self
     */
    public function setDescription($description)
    {
        if (is_null($description)) {
            array_push($this->openAPINullablesSetToNull, 'description');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('description', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['description'] = $description;

        return $this;
    }

    /**
     * Gets unitPrice
     *
     * @return float|null
     */
    public function getUnitPrice()
    {
        return $this->container['unitPrice'];
    }

    /**
     * Sets unitPrice
     *
     * @param float|null $unitPrice unitPrice
     *
     * @return self
     */
    public function setUnitPrice($unitPrice)
    {
        if (is_null($unitPrice)) {
            array_push($this->openAPINullablesSetToNull, 'unitPrice');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('unitPrice', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['unitPrice'] = $unitPrice;

        return $this;
    }

    /**
     * Gets currencyCode
     *
     * @return string|null
     */
    public function getCurrencyCode()
    {
        return $this->container['currencyCode'];
    }

    /**
     * Sets currencyCode
     *
     * @param string|null $currencyCode currencyCode
     *
     * @return self
     */
    public function setCurrencyCode($currencyCode)
    {
        if (is_null($currencyCode)) {
            array_push($this->openAPINullablesSetToNull, 'currencyCode');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('currencyCode', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['currencyCode'] = $currencyCode;

        return $this;
    }

    /**
     * Gets itemCount
     *
     * @return int
     */
    public function getItemCount()
    {
        return $this->container['itemCount'];
    }

    /**
     * Sets itemCount
     *
     * @param int $itemCount itemCount
     *
     * @return self
     */
    public function setItemCount($itemCount)
    {
        if (is_null($itemCount)) {
            throw new \InvalidArgumentException('non-nullable itemCount cannot be null');
        }
        $this->container['itemCount'] = $itemCount;

        return $this;
    }

    /**
     * Gets weightInGram
     *
     * @return int|null
     */
    public function getWeightInGram()
    {
        return $this->container['weightInGram'];
    }

    /**
     * Sets weightInGram
     *
     * @param int|null $weightInGram weightInGram
     *
     * @return self
     */
    public function setWeightInGram($weightInGram)
    {
        if (is_null($weightInGram)) {
            array_push($this->openAPINullablesSetToNull, 'weightInGram');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('weightInGram', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['weightInGram'] = $weightInGram;

        return $this;
    }

    /**
     * Gets shippingAllowed
     *
     * @return bool
     */
    public function getShippingAllowed()
    {
        return $this->container['shippingAllowed'];
    }

    /**
     * Sets shippingAllowed
     *
     * @param bool $shippingAllowed That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined.
     *
     * @return self
     */
    public function setShippingAllowed($shippingAllowed)
    {
        if (is_null($shippingAllowed)) {
            throw new \InvalidArgumentException('non-nullable shippingAllowed cannot be null');
        }
        $this->container['shippingAllowed'] = $shippingAllowed;

        return $this;
    }

    /**
     * Gets handDeliveryAllowed
     *
     * @return bool
     */
    public function getHandDeliveryAllowed()
    {
        return $this->container['handDeliveryAllowed'];
    }

    /**
     * Sets handDeliveryAllowed
     *
     * @param bool $handDeliveryAllowed Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product.
     *
     * @return self
     */
    public function setHandDeliveryAllowed($handDeliveryAllowed)
    {
        if (is_null($handDeliveryAllowed)) {
            throw new \InvalidArgumentException('non-nullable handDeliveryAllowed cannot be null');
        }
        $this->container['handDeliveryAllowed'] = $handDeliveryAllowed;

        return $this;
    }

    /**
     * Gets shippingCarriers
     *
     * @return string[]
     */
    public function getShippingCarriers()
    {
        return $this->container['shippingCarriers'];
    }

    /**
     * Sets shippingCarriers
     *
     * @param string[] $shippingCarriers If you wish to enable automated shipping label generation through a specific provider, specify it there.
     *
     * @return self
     */
    public function setShippingCarriers($shippingCarriers)
    {
        if (is_null($shippingCarriers)) {
            throw new \InvalidArgumentException('non-nullable shippingCarriers cannot be null');
        }
        $allowedValues = $this->getShippingCarriersAllowableValues();
        if (array_diff($shippingCarriers, $allowedValues)) {
            throw new \InvalidArgumentException(
                sprintf(
                    "Invalid value for 'shippingCarriers', must be one of '%s'",
                    implode("', '", $allowedValues)
                )
            );
        }
        $this->container['shippingCarriers'] = $shippingCarriers;

        return $this;
    }

    /**
     * Gets eanCode
     *
     * @return string|null
     */
    public function getEanCode()
    {
        return $this->container['eanCode'];
    }

    /**
     * Sets eanCode
     *
     * @param string|null $eanCode eanCode
     *
     * @return self
     */
    public function setEanCode($eanCode)
    {
        if (is_null($eanCode)) {
            array_push($this->openAPINullablesSetToNull, 'eanCode');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('eanCode', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['eanCode'] = $eanCode;

        return $this;
    }

    /**
     * Gets metadata
     *
     * @return \Tripartie\Tpdk\Model\MetadataUpdate[]
     */
    public function getMetadata()
    {
        return $this->container['metadata'];
    }

    /**
     * Sets metadata
     *
     * @param \Tripartie\Tpdk\Model\MetadataUpdate[] $metadata metadata
     *
     * @return self
     */
    public function setMetadata($metadata)
    {
        if (is_null($metadata)) {
            throw new \InvalidArgumentException('non-nullable metadata cannot be null');
        }
        $this->container['metadata'] = $metadata;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset): bool
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed|null
     */
    #[\ReturnTypeWillChange]
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset): void
    {
        unset($this->container[$offset]);
    }

    /**
     * Serializes the object to a value that can be serialized natively by json_encode().
     * @link https://www.php.net/manual/en/jsonserializable.jsonserialize.php
     *
     * @return mixed Returns data which can be serialized by json_encode(), which is a value
     * of any type other than a resource.
     */
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
       return ObjectSerializer::sanitizeForSerialization($this);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


